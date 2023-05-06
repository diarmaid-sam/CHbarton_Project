import ttkbootstrap.tableview as tbtable

import sqlite3
import datetime

# 'Enter' Button widget for ItemDetails top-level frame now updates the products db table, changes the AddItem frame switch to the expiry date + quantity entry frame and closes the ItemDetails top-level frame (all this packed into 'finish_btn_click' function. The function also calls 'add_update_item' function from db_queries.py (also a new function which queries the db.


## GLOBAL 1: list of all users 
conn = sqlite3.connect("shop_inventory.db")
c = conn.cursor()
c.execute("""SELECT username FROM users;""")
users_list = c.fetchall()
c.close()

## queries database based on provided parameters
def get_table_data(including_rows, condition,  query_type, make_table, **kwargs):
    conn = sqlite3.connect("shop_inventory.db")
    c = conn.cursor()

    if query_type == 'all':
        if condition == None:
            query_structure = """SELECT {cols} FROM inventory 
            JOIN products ON inventory.product_id = products.product_id 
            JOIN users ON products.user_id = users.user_id;"""
            query = query_structure.format(cols=", ".join(including_rows))
        else:
            query_structure = """SELECT {cols} FROM inventory 
            JOIN products ON inventory.product_id = products.product_id 
            JOIN users ON products.user_id = users.user_id
            {cond};"""
            query = query_structure.format(cols=", ".join(including_rows), cond=condition)
    ## enables individual tables to be queried
    else:
        if condition == None:
            query_structure = """SELECT {cols} FROM {table};"""
            query = query_structure.format(cols=", ".join(including_rows), table=query_type)
        else:
            query_structure = """SELECT {cols} FROM {table} {cond};"""
            query = query_structure.format(cols=", ".join(including_rows), cond=condition, table=query_type)


    

    c.execute(query)
   
    rowdata = c.fetchall()
    c.close()
    if make_table:
        coldata = []
        for i, colname in enumerate(including_rows):
            # changes the original column name into a more user-friendly format
            dict_entry = {'text':None, 'stretch': True}
            colname = colname.replace("_", " ")
            colname = colname.replace("users.", "")
            colname = colname.replace("products.", "")
            colname = colname.replace("inventory.", "")
            dict_entry['text'] = colname
            coldata.append(dict_entry)

        table = tbtable.Tableview(master=(kwargs.get('master')), 
                                          coldata=coldata, 
                                          rowdata=rowdata,
                                          searchable=kwargs.get('searchable'),
                                          stripecolor=('gray', 'white'))
        
        
        return table
    return rowdata

def add_update_item(item_name, username, item_id=None):
    conn = sqlite3.connect("shop_inventory.db")
    c = conn.cursor()

    c.execute("SELECT user_id FROM users WHERE username = (?)", (username,))
    username_id = c.fetchone()
    # if ItemDetails toplevel was created from 'New item' btn widget, then no item_id will be passed (since it's just being created)
    if item_id == None:
        c.execute("INSERT INTO products (product_name, user_id) VALUES (?, ?)", ((item_name, username_id[0])))
    # else it's modifying pre-existing 
    else:
        c.execute("UPDATE products SET product_name = ?, user_id = ? WHERE product_id = ?", ((item_name, username_id[0], item_id)))

    conn.commit()
    c.close()
    return

def submit_addItems(product_id, exp_month, exp_year, quantity):

    conn = sqlite3.connect("shop_inventory.db")
    c = conn.cursor()

    # getting the date and time now 
    datenow = datetime.datetime.now()
    formatted_date = datenow.strftime("%Y-%m-%d %H:%M:%S")
    
    print(product_id, exp_month, exp_year, quantity, formatted_date)
    c.execute("INSERT INTO inventory (expiry_date_month, expiry_date_year, quantity, date_added, product_id) VALUES (?, ?, ?, ?, ?)", (exp_month, exp_year, quantity, formatted_date, product_id))

    conn.commit()
    c.close()
    return