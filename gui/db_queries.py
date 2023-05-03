import ttkbootstrap.tableview as tbtable

import sqlite3


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
    print(query, rowdata)
    if make_table:
        coldata = []
        for i, colname in enumerate(including_rows):
            dict_entry = {'text':None, 'stretch': True}

            # changes the original column name into a more user-friendly format
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