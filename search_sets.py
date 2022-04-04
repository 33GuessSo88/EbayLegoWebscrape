"""
- Creates a connection to the db
- Extracts the column SetNum where pieces > 1 as a dataframe
- Removes -1 from set num
- Creates a list from the SetNum column of df
- Returns this list called search_terms
"""




def create_search_list():

    import pandas as pd
    import sqlite3

    # create a connection to the database
    connection = sqlite3.connect('lego.db')
    cursor = connection.cursor()

    query1 = ''' SELECT DISTINCT SetNum
            FROM brickset_set_nums
            WHERE NumPieces > 0
    '''

    df = pd.read_sql_query(query1, connection)

    connection.close()

    # remove -1 from set_num
    df['SetNum'] = df['SetNum'].str.split('-', n=1).str[0]

    # create list from df column
    search_terms = df['SetNum'].tolist()

    # Remove duplicates
    search_terms = list(dict.fromkeys(search_terms))
    search_terms.sort(reverse=True)
    # print(search_terms)
    # print(len(search_terms))


    return search_terms



# TODO: Go to brickset.com every 3 months and grab a new set of set numbers.

# create_search_list()