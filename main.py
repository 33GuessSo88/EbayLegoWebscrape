from bs4 import BeautifulSoup
import pandas as pd
import requests
from datetime import date
from urllib.parse import urlparse
from search_sets import search_terms

# searchterm = ['21033',
#               '75827'
#               ]

today = date.today()
today = today.strftime("%m-%d-%Y")


def get_data(term):
    url = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw="lego"+"{term}"&_sacat=0&Packaging=Box&_dcat=19006&LH_ItemCondition=1000&rt=nc&LH_BIN=1'
    r = requests.get(url)
    print(r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def parse(soup):
    productslist = []
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
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
            link = item.find('a', {'class': 's-item__link'})['href']
            print(link)
            parts = urlparse(link)
            directories = parts.path.strip('/').split('/')
            item_num = directories[1]
            print(item_num)
        product = {
            'date': today,
            'setID': term,
            'link': link,
            'item_num': item_num,
            'price': price
        }
        print(product)
        productslist.append(product)
    return productslist


def output(productslist, term):
    productsdf = pd.DataFrame(productslist)
    productsdf.to_csv(f'LEGO{term}_{today}.csv', index=False)
    print("Saved to csv")
    return


for term in search_terms:
    soup = get_data(term)
    productslist = parse(soup)
    output(productslist, term)
