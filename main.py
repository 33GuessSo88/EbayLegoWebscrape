"""Ebay Webscraper

This script will take a list of Lego sets, scrape the Buy It Now prices from Ebay,
and save the data in a csv for each set
"""

from bs4 import BeautifulSoup
import pandas as pd
import requests
from datetime import date
from urllib.parse import urlparse
import search_sets
import sqlite3
import time
from random import randint
from send_sms import send_message


def get_data(term):
    """Returns a beautiful soup object from a single page of Ebay Buy It Now items.
    :term: a Lego set number that is searched on
    """
    url = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw="lego"+"{term}"&_sacat=0&Packaging=Box&_dcat=19006' \
          f'&LH_ItemCondition=1000&rt=nc&LH_BIN=1 '
    r = requests.get(url)
    # print(r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def parse(soup):
    """Returns a list of sale items for one Lego set number.
    :soup: a beautiful soup object
    """

    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    # Had a major problem with this div, the first one was usually blank,
    # so added the first if statement. Should probably use a try except block.
    # TODO: replace if statement with try except blocks
    # TODO: add logging functionality
    # print(len(results))
    # print(type(results))
    # print(type(results[0]))
    for item in results:
        if item.find('span', {'class': 's-item__price'}):
            price = item.find('span', {'class': 's-item__price'}).text.replace('$', '')
            # print(price)
        else:
            continue
        if item.find('a', {'class': 's-item__link'})['href']:
            link = item.find('a', {'class': 's-item__link'})['href']  # this is the full href
            # print(link)
            parts = urlparse(link)  # I want the item number in the href, use it as primary key in db
            directories = parts.path.strip('/').split('/')
            item_num = directories[1]
            # print(item_num)

        cursor.execute('''INSERT OR IGNORE INTO ebay_prices VALUES (?, ?, ?, ?, ?)''',
                            (item_num, term, today, price, link))


# To calculate how long script runs we need time now
start_time = time.time()
# Also need date for db entries
today = date.today()
today = today.strftime("%m-%d-%Y")

# Create list of sets to loop over
search_terms = search_sets.create_search_list()

# Create connection to db and a cursor to execute commands
connection = sqlite3.connect('lego.db')
cursor = connection.cursor()

for term in search_terms:
    rows_before = cursor.execute('''SELECT * FROM ebay_prices''')
    rows_before = len(rows_before.fetchall())
    print(f"Records before insertion: {rows_before}")
    soup = get_data(term)
    productslist = parse(soup)
    time.sleep(randint(0,2))
    rows_after = cursor.execute('''SELECT * FROM ebay_prices''')
    rows_after = len(rows_after.fetchall())
    print(f"Records after insertion: {rows_after}")
    print("Total rows added: ", rows_after - rows_before)

connection.commit()
connection.close()

end_time = time.time()
print("Execution time is: ", end_time-start_time)
send_message()
