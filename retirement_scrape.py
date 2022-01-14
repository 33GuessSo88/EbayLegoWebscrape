"""retirement date scraper

This script will take a list of lego sets and scrape brickset for retirement date, etc
"""

from bs4 import BeautifulSoup
import pandas as pd
import requests
import sqlite3

list_of_sets = [2235, 2236]

feature_info = pd.DataFrame()
columns = []
values = []

for set_num in list_of_sets:
    new_values = []
    url = f'https://brickset.com/sets/{set_num}'
    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")

    info = soup.find_all("section", {'class': 'featurebox'})

    for i in info[0].find_all('dt'):
        columns.append(i.text)

    for i in info[0].find_all('dd'):
        new_values.append(i.text)
    # Split all elements of new_values at ' - ' to separate Launch Exit dates
    # This also split age from to so I just added another column, too hard to concatenate
    values2 = []
    for i in new_values:
        values2 += i.split(' - ')
    # Split set number to remove -1
    values2 = [i.split('-', 1)[0] for i in values2]
    values.append(values2)

print(columns)
print(values)

connection = sqlite3.connect('lego.db')
cursor = connection.cursor()

sql_statement = 'INSERT INTO details VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
cursor.executemany(sql_statement, values)
connection.commit()
connection.close()