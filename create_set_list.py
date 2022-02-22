""" This file grabs the brickset_set_nums table from the lego.db
and parses out the set_num in a clean format
and then saves as a csv for search_set.py to use
"""

import sqlite3
import pandas as pd

# create a connection to the database
connection = sqlite3.connect('lego.db')
cursor = connection.cursor()

query1 = ''' SELECT DISTINCT SetNum
            FROM brickset_set_nums
            WHERE NumPieces > 0
'''

df = pd.read_sql_query(query1, connection)
# print(df)

# remove -1 from set_num
df['SetNum'] = df['SetNum'].str.split('-', n=1).str[0]
# print(df)

df.to_csv('list_of_all_sets.csv', index=False)