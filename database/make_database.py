import sqlite3

# create database/start connection with database
conn = sqlite3.connect("shop_inventory.db")

# create cursor to navigate database
c = conn.cursor()
# TODO fix this query, needs a functioning IF statement which enables the verifying of existing tables in the shop inventory database
c.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='inventory';""")

table_exists = c.fetchall()

if len(table_exists) == 0:
    print("here2")

    c.execute("""CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    product_section TEXT NOT NULL
    );""")

    c.execute("""CREATE TABLE inventory (
    id INTEGER PRIMARY KEY,
    expiry_date TEXT NOT NULL,
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
