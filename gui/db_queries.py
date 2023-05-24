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
        # here if 'state' is true, i.e. has a value, then the table to be created is interactable and so double-clicking column calls the double_click function
        if kwargs.get('state'):
            # master is where the ItemDetails toplevel is to be placed, event is the event object, state is the type of toplevel created (i.e. used for adding items or editting item details) and top_level is optional, used only if state='add' (enables the adding_frame to be tkraised)
            table.bind_all("<Double-1>", lambda event: double_click(kwargs.get('master'), event, kwargs.get('state'), kwargs.get('top_level')))
        
        return table
    return rowdata

def double_click(self, event, state, tlf):
        from toplevel_windows import ItemDetails
        # retrieve the id of the row selected and get it's 'values' (stored in a dictionary)
        item = event.widget.focus()
        item_details = (event.widget.item(item, 'values'))
        # for sake of a standard, the product name will always come first in a table (if the table is to be interactable), therefore we can say the product_name is at element '0'
        product_name = item_details[0]
        product_id = get_table_data(['product_id'], f'WHERE product_name = "{product_name}"', 'products', False)[0][0]
        ItemDetails(product_id, state, tlf)
        # def __init__(self, item_id=None, state="add", top_level_frame=None, themename="superhero"):
    

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
    
    # sumbit info to relevant table
    c.execute("INSERT INTO inventory (expiry_date_month, expiry_date_year, quantity, date_added, product_id) VALUES (?, ?, ?, ?, ?)", (exp_month, exp_year, quantity, formatted_date, product_id))

    conn.commit()
    c.close()
    return

# type = the type of items being selected for (expired, shortdated or all); rows = wheterh the item rows (themselves) are being selected for or item quantities
def item_state(type="all", rows=False):
    conn = sqlite3.connect("shop_inventory.db")
    c = conn.cursor()

    current_date = datetime.datetime.now()

    # Format date as string
    curr_month = current_date.month
    curr_year = current_date.year

    sd_var = (3)-1
    m_upperbound = 1 if curr_month + sd_var == 13 else 2
    selected_col = 'SUM(quantity)' if rows == False else '*'
    
    if type == "expired":
        # formated string for querying expiry dates
        query = f"""SELECT {selected_col} FROM inventory 
        WHERE expiry_date_year < {curr_year} 
        OR expiry_date_year == {curr_year} AND expiry_date_year < {curr_month};"""
        # number of expired items (of a year less than )
        c.execute(query)
        count = c.fetchone()[0] if rows == False else c.fetchall()
        
    elif type == "short":
        if curr_month >= 11:
            # ternary operator to assign the upper bound month to variable (1 if month is 11th or 2 if month is 12)
            # TODO not curr flexible to changing definition of short-dated. can be modified later
            
            query = f"""SELECT {selected_col} FROM inventory 
            WHERE expiry_date_year == {curr_year} AND expiry_date_month <= 12 AND expiry_date_month >= {curr_month}
            OR expiry_date_year == {curr_year + 1} AND expiry_date_month <= {m_upperbound};"""
            c.execute(query)   
            
        else:
            query = f"""SELECT {selected_col} FROM inventory 
            WHERE expiry_date_year == {curr_year} AND expiry_date_month >= {curr_month} AND expiry_date_month <= {curr_month + sd_var};"""
            c.execute(query)
        count = c.fetchone()[0] if rows == False else c.fetchall()
        
    else:
        query = f"SELECT {selected_col} FROM inventory;"
        c.execute(query)
        count = c.fetchone()[0] if rows == False else c.fetchall()

        ## CODE FOR COUNTING 'IN-DATE' ITEMS [NOT IN USE]
        # if curr_month >= 11:
        #     query = f"""SELECT {selected_col} FROM inventory
        #     WHERE expiry_date_year == {curr_year + 1} AND expiry_date_month >= {m_upperbound}"""
        #     c.execute("")
        # else:
        #     query = f"""SELECT {selected_col} FROM inventory
        #     WHERE expiry_date_year == {curr_year} AND expiry_date_month >= {curr_month + sd_var};
        #     """
    
    
    # check the return value isn't none
    count = count if count != None else 0
    return count
    c.close()