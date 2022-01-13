"""retirement date scraper

This script will take a list of lego sets and scrape brickset for retirement date, etc
"""

from bs4 import BeautifulSoup
import pandas as pd
import requests

list_of_sets = [2235, 2236]


for set_num in list_of_sets:
    url = f'https://brickset.com/sets/{set_num}'
    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")

    info = soup.find_all("section", {'class': 'featurebox'})

    feature_info = pd.DataFrame()

    cleaned_id_text = []
    for i in info[0].find_all('dt'):
        cleaned_id_text.append(i.text)
    print(cleaned_id_text)
    new_list = [y for x in cleaned_id_text for y in x.split('/')]
    even_newer_list = [i.strip() if type(i) == str else str(i) for i in new_list]
    print(even_newer_list)
    # print(cleaned_id_text)

    cleaned_id_value_text = []
    for i in info[0].find_all('dd'):
        cleaned_id_value_text.append(i.text)
    print(cleaned_id_value_text)
    # Can't figure out how to only split at index 7
    new_values = [y for x in cleaned_id_value_text for y in x.split('-', 1)]
    print(new_values)
    # Shit, this was tough. Had to join the first split back together
    new_values[0:2] = ['-'.join(new_values[0:2])]
    # lists are immutable, so need to create new list name
    even_newer_values = [i.strip() if type(i) == str else str(i) for i in new_values]
    print(even_newer_values)

    feature_info['Id'] = cleaned_id_text
    feature_info['Value'] = cleaned_id_value_text
    print(feature_info)
    feature_info.set_index('Id', inplace=True)
    # Transpose rows to colums
    feature_info_t = feature_info.T
    print(feature_info_t)
    for col in feature_info_t:
        print(col)
    feature_info_t.drop(columns=['Tags', 'Current value', 'Price per piece', 'Weight',
                                 'Dimensions', 'Barcodes', 'LEGO item numbers'],
                        inplace=True)
    print(feature_info_t)
    # split Launch/exit into 2 columns
    # I think exit is a special word, need to replace it
    feature_info_t.columns = feature_info_t.columns.str.replace('/', '_')
    feature_info_t.columns = feature_info_t.columns.str.replace('exit', 'retirement')
    print(feature_info_t['Launch_retirement'])
    feature_info_t[['Launch Date', 'Retirement Date']] = feature_info_t.Launch_retirement.str.split(' - ', expand=True)
    feature_info_t = feature_info_t['Rating'].str.split().str[1]
    print(feature_info_t)

