"""Ebay Webscraper

This script will take a list of Lego sets, scrape the Buy It Now prices from Ebay,
and save the data in a csv for each set
"""

from bs4 import BeautifulSoup
import pandas as pd
import requests
from datetime import date
from urllib.parse import urlparse
from search_sets import search_terms

# below is for testing only
# searchTerm = ['21033',
#               '75827'
#               ]

today = date.today()
today = today.strftime("%m-%d-%Y")


def get_data(term):
    """Returns a beautiful soup object from a single page of Ebay Buy It Now items.
    :term: a Lego set number that is searched on
    """
    url = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw="lego"+"{term}"&_sacat=0&Packaging=Box&_dcat=19006' \
          f'&LH_ItemCondition=1000&rt=nc&LH_BIN=1 '
    r = requests.get(url)
    print(r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def parse(soup):
    """Returns a list of sale items for one Lego set number.
    :soup: a beautiful soup object
    """
    productslist = []
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    # Had a major problem with this div, the first one was usually blank,
    # so added the first if statement. Should probably use a try except block.
    # TODO: replace if statement with try except blocks
    # TODO: add logging functionality
    print(len(results))
    print(type(results))
    print(type(results[0]))
    for item in results:
        if item.find('span', {'class': 's-item__price'}):
            price = item.find('span', {'class': 's-item__price'}).text.replace('$', '')
            print(price)
        else:
            price = 'null'
        if item.find('a', {'class': 's-item__link'})['href']:
            link = item.find('a', {'class': 's-item__link'})['href']  # this is the full href
            print(link)
            parts = urlparse(link)  # I want the item number in the href, use it as primary key in db
            directories = parts.path.strip('/').split('/')
            item_num = directories[1]
            print(item_num)
        product = {
            'date': today,
            'setID': term,
            'link': link,
            'item_num': item_num,  # use as primary key in db to limit repeats
            'price': price
        }
        print(product)
        productslist.append(product)
    return productslist


def output(productslist, term):
    """Saves a csv of one set number.
    :productslist: a list of sale items for one LEgo set number
    :term: a Lego set number
    """
    # TODO: replace writing to csv with writing to a database
    productsdf = pd.DataFrame(productslist)
    productsdf.to_csv(f'LEGO{term}_{today}.csv', index=False)
    print("Saved to csv")
    return


for term in search_terms:
    soup = get_data(term)
    productslist = parse(soup)
    output(productslist, term)
