""" 
- Creates a connection to the db
- Extracts the column SetNum where pieces>1 as a dataframe
- removes -1 from set num
- saves as csv to be used later by search_sets.py

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

connection.close()

# remove -1 from set_num
df['SetNum'] = df['SetNum'].str.split('-', n=1).str[0]
# print(df)

df.to_csv('list_of_all_sets.csv', index=False)