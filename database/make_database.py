import sqlite3

# create database/start connection with database
conn = sqlite3.connect("shop_inventory.db")

# create cursor to navigate database
c = conn.cursor()

# checks if the tables have already been created locally. If not then create them, else, skip
c.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='inventory';""")

# the name of the table is returned, hence len() is used later on
table_exists = c.fetchall()

if len(table_exists) == 0:

    # product id here in products will be the barcode that is generated (that's the plan at least)
    c.execute("""CREATE TABLE users (
    user_id INTEGER NOT NULL PRIMARY KEY,
    username TEXT NOT NULL
    );""")

    c.execute("""CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    user_id  INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (user_id)    
    );""")

    c.execute("""CREATE TABLE inventory (
    id INTEGER PRIMARY KEY,
    expiry_date_month INTEGER NOT NULL,
    expiry_date_year INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    date_added TEXT NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products (product_id)
    );
        """)



# commit changes made to database
conn.commit()

# close connection to database
c.close()
