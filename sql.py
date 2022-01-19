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


def create_set_details():
    connection = sqlite3.connect('lego.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS set_details
                                (set_num TEXT PRIMARY KEY NOT NULL, 
                                set_name TEXT,  
                                theme_group TEXT, 
                                theme TEXT,
                                subtheme TEXT,
                                year_released TEXT,
                                launch_exit TEXT,
                                pieces INTEGER,
                                minifigs TEXT,
                                designer TEXT,
                                msrp TEXT,
                                age_range TEXT,
                                packaging TEXT,
                                availability TEXT,
                                rating TEXT)
                        ''')
    connection.close()

create_set_details()