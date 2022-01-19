"""retirement date scraper

This script will take a list of lego sets and scrape brickset for retirement date, etc
"""

from bs4 import BeautifulSoup
import requests
import sqlite3
import time
from random import randint
import search_sets
import logging

logging.basicConfig(filename='retirement.log', filemode='a', level=logging.ERROR)

# Create list of sets to loop over
list_of_sets = search_sets.create_search_list()
# list_of_sets = [60009, 60010, 60012, 75975]  # for testing

dict_keys = ['Set number', 'Name', 'Theme group', 'Theme', 'Subtheme', 'Year released', 'Launch/exit',
             'Pieces', 'Minifigs', 'Designer', 'RRP', 'Age range', 'Packaging', 'Availability', 'Rating']


def get_dl(soup):
    keys, values = [], []
    for section in soup.find_all("section", {'class': 'featurebox'}):
        for dl in section.find_all("dl"):
            for dt in dl.find_all("dt"):
                keys.append(dt.text.strip())
            for dd in dl.find_all("dd"):
                values.append(dd.text.strip())
            return dict(zip(keys, values))

# Create connection to database
connection = sqlite3.connect('lego.db')
cursor = connection.cursor()

# count initial rows in db before we make changes
initital_rows = cursor.execute('''SELECT * FROM set_details''')
initital_rows = len(initital_rows.fetchall())
print(f'Initial rows: {initital_rows}')

for set_num in list_of_sets:
    try:
        time.sleep(randint(3, 10))
        print(set_num)
        url = f'https://brickset.com/sets/{set_num}'
        page = requests.get(url)

        soup = BeautifulSoup(page.text, "html.parser")

        set_dict = get_dl(soup)

        # Check list of dictionary keys, if it doesn't exist, add it with value None
        for key in dict_keys:
            if key not in set_dict:
                set_dict[key] = None
        # print(set_dict)

        # filter dictionary to only keys in dict_keys list for easy SQL insertion
        filtered_dict = {}
        for key, value in set_dict.items():
            if key in dict_keys:
                filtered_dict[key] = value
        # print(filtered_dict)
        # print(len(filtered_dict))

        # write one set of data to database, but only one commit after the for loop
        cursor.execute("INSERT OR IGNORE INTO set_details VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       [filtered_dict["Set number"],
                        filtered_dict["Name"],
                        filtered_dict["Theme group"],
                        filtered_dict["Theme"],
                        filtered_dict["Subtheme"],
                        filtered_dict["Year released"],
                        filtered_dict["Launch/exit"],
                        filtered_dict["Pieces"],
                        filtered_dict["Minifigs"],
                        filtered_dict["Designer"],
                        filtered_dict["RRP"],
                        filtered_dict["Age range"],
                        filtered_dict["Packaging"],
                        filtered_dict["Availability"],
                        filtered_dict["Rating"]
                        ]
                       )
    except:
        pass
# commit all changes to db
connection.commit()

# find number of rows in db after commit
final_rows = cursor.execute('''SELECT * FROM set_details''')
final_rows = len(final_rows.fetchall())
print(f"Final rows: {final_rows}")

connection.close()
