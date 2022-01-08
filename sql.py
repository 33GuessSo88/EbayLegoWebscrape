import sqlite3


def create_db():
    connection = sqlite3.connect('lego.db')  # connect to database
    cursor = connection.cursor()  # create cursor that executes commands

    cursor.execute('''CREATE TABLE IF NOT EXISTS ebay_prices
                            (item_num INTEGER PRIMARY KEY, 
                            set_num INTEGER, 
                            date TEXT, 
                            price REAL, 
                            link TEXT)
                    ''')
    connection.close()


