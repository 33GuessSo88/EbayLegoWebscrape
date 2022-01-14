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

def create_details():
    connection = sqlite3.connect('lego.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS details
                                (set_num INTEGER PRIMARY KEY, 
                                name TEXT, 
                                set_type TEXT, 
                                theme_group TEXT, 
                                theme TEXT,
                                subtheme TEXT,
                                year_released INTEGER,
                                launch_date TEXT,
                                retirement_date TEXT,
                                tags TEXT,
                                pieces INTEGER,
                                msrp REAL,
                                current_value REAL,
                                price_per_piece REAL,
                                age_from INTEGER,
                                age_to INTEGER,
                                packaging TEXT,
                                dimensions TEXT,
                                weight TEXT,
                                barcode TEXT,
                                lego_item_num TEXT,
                                availability TEXT,
                                rating TEXT)
                        ''')
    connection.close()

# create_details()