import sqlite3

# create database/start connection with database
conn = sqlite3.connect("shop_inventory.db")

# create cursor to navigate database
c = conn.cursor()


# commit changes made to database
conn.commit()

# close connection to database
c.close()
