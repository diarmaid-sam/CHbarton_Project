from tkinter import *
from tkinter import Tk
from tkinter import ttk
import ttkbootstrap as tb
import sqlite3
import datetime

from button_mappings import calc_layout
from db_queries import *


# what is necessary:
# scan item - If the barcode is registered in the database, then the fields are automatically filled. If the barcode isn't registered, then the 'register product' comes up.
# Quantity - The number of products (make it like a calculator, with big buttons for input)
# Expiry date 

class AddItems(tb.Toplevel):
    def __init__(self, master, themename="superhero"):
        super().__init__(title="Add Items", size=(1000, 800), resizable=(False, True))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)  
        self.product_id = None
        global placeholder_list
        global calc_key1
        # lists are necessary as updating values using int or str data_types causes issues
        placeholder_list = ['', '']
        calc_key1 = [0]
        
        ## DEFAULT FRAME
        self.default_frame = tb.Frame(self, bootstyle='danger')
        self.default_frame.grid(column=0, row=0, sticky='nsew')
        self.default_frame.columnconfigure(0, weight=1)
        self.default_frame.rowconfigure(0, weight=1)

        default_frame_prompt = tb.Label(self.default_frame, text="scan an item to get started", bootstyle='light')
        default_frame_prompt.grid(column=0, row=0, sticky='nsew')
        default_frame_prompt.config(font=('Arial', 20))
        default_frame_prompt.configure(anchor='center', justify='center')

        # mimic the scanning of a product (can only be called if default_frame is in focus)
        

        ## possibly create AddItem_frame when a new item item is being added (and then destroy it afterwards, so that it refreshes)
        

        self.AddItem_frame()
        self.default_frame.tkraise()
        self.default_frame.focus()
        self.grid()

        self.bind('<Control-Return>', self.on_scan)


    def on_scan(self, event):
        # mimics the scanning of an item TODO: replace this with an if statement verifying whether scanning has taken place
        if event.state & 4 and event.keysym == 'Return':
            self.unknown_barcode()
            return
        
    # TODO function for when pressing row, for ItemDetails to show up
    # def show_item_details(self, event):
       
    #     return
    #     ItemDetails(self, self)
    
    def unknown_barcode(self):
        self.unknown_frame = tb.Frame(self)
        self.unknown_frame.grid(column=0, row=0, sticky='nsew')
        self.unknown_frame.columnconfigure(0, weight=1)
        self.unknown_frame.rowconfigure(2, weight=1)

        randbtn = tb.Button(self.unknown_frame, text='fk').grid(column=0, row=3)

        # command here does not pass any item_id since it's creating a new item
        new_item_btn = tb.Button(self.unknown_frame, text='New Item?', padding=(30, 10), command=lambda:ItemDetails(self, item_id=None))
        new_item_btn.grid(column=0, row=0, pady=10)
        search_label = tb.Label(self.unknown_frame, text='or Search existing items')
        search_label.grid(column=0, row=1, sticky='new', pady=(0, 10))
        search_label.config(anchor='center', font=('Arial', 14))
        table = get_table_data(['products.user_id', 'product_name'], condition=None, query_type='products' ,make_table=True, master=self.unknown_frame, searchable=True)
        table.grid(column=0, row=2, sticky='nsew', padx=10, pady=5)

    
        # TODO Implement on select of table row, bring up ItemDetails class window
        # self.bind('<<TreeviewSelect>>', self.show_item_details)

    def calcAPI(self, *args, key1, key2, placeholder_list):
        if key2 == "add":
            # if you are entering the expirey date string, the following rules apply (and the relevant date widget is updated)
            if key1 == 0:
                # 7 is max characters for the date, hence it prevents further input once 7 characters is reached
                if len(placeholder_list[key1]) == 7:
                    return placeholder_list[key1]
                # stops the addition of a number if it has reached max 7
                placeholder_list[key1] += args[0]
                # if 2 characters is reached, is implies the month is entered, and so a slash is automatically entered
                if len(placeholder_list[key1]) == 2:
                    placeholder_list[key1] += '/'
                self.date.set(placeholder_list[key1])
                return placeholder_list
            # else, you modify the quantity label widget
            else:
                placeholder_list[key1] += args[0]
                self.quantity.set(placeholder_list[key1])
                return placeholder_list
                
        elif key2 == "back":            
            # if the last value of the string is a '/' char, remove an additional char from the str
            if len(placeholder_list[key1]) > 0:
                if placeholder_list[key1][-1] == '/':
                    placeholder_list[key1] = placeholder_list[key1][:-1] 

                # even if none of the above apply, still remove the last digit
                placeholder_list[key1] = placeholder_list[key1][:-1]
                # update value of label widget
                if key1 == 0:
                    self.date.set(placeholder_list[key1])
                else:
                    self.quantity.set(placeholder_list[key1])

                return placeholder_list
            
            # if you backspace on an empty 'quantity string' then it will take you back to the 'expirey date string'
            if key1 == 1:
                calc_key1[0] = 0
                # calc_key is updated as is the global variable keeping track of the key1 value
        # else = when the done button is pressed.
        else:
            if key1 == 1: 
                # sumbit placeholder_list to database
                # TODO needs to submit month and year separately
                # clear placeholder_list
                placeholder_list = ['', '']
                self.date.set(placeholder_list[0])
                self.quantity.set(placeholder_list[1])

                return placeholder_list
            elif len(placeholder_list[key1]) == 7:
                calc_key1[0] = 1
                return

        
    # This frame is the one where (once the item type is confirmed) the item's quantity and expiry date are inputted and put into the database
    def AddItem_frame(self):
        self.adding_frame = tb.Frame(self, width=1000, height=800)
        self.adding_frame.grid(column=0, row=0, sticky='nsew')
        self.adding_frame.columnconfigure(0, weight=15)
        self.adding_frame.columnconfigure(1, weight=2)
        self.adding_frame.rowconfigure(0, weight=1)
        self.adding_frame.rowconfigure(1, weight=7)

        # the frame where the numbers typed will appear to the user. Large box situated top of the screen  
        self.input_display = tb.Frame(self.adding_frame, width=((1000*6)/8), height=(800/7), relief='solid')
        self.input_display.grid(column=0, row=0, sticky='nsew', padx=10, pady=15)

        self.input_display.columnconfigure(0, weight=1)
        self.input_display.rowconfigure(0, weight=1)
        self.input_display.rowconfigure(1, weight=1)

        # variable to store the inputs of the digit panel   
        self.date = StringVar()
        self.quantity = StringVar()
    
        self.date.set("month/year")
        self.quantity.set("e.g. 12")

        self.date_frame = tb.LabelFrame(self.input_display, text=" Date ",border=1, relief='solid', padding=10)
        self.date_frame.columnconfigure(0, weight=1)
        self.date_frame.rowconfigure(0, weight=1)
        self.date_frame.grid(column=0, row=0, sticky='nsew', pady=5, padx=5)

        self.quantity_frame = tb.LabelFrame(self.input_display, text=" Quantity ",border=1, relief='solid', padding=10)
        self.quantity_frame.columnconfigure(0, weight=1)
        self.quantity_frame.rowconfigure(0, weight=1)
        self.quantity_frame.grid(column=0, row=1, sticky='nsew', pady=5, padx=5)

        self.date_label = tb.Label(self.date_frame, textvariable=self.date)
        self.date_label.grid(column=0, row=0, sticky='ns')
        self.quantity_label = tb.Label(self.quantity_frame, textvariable=self.quantity)
        self.quantity_label.grid(column=0, row=0, sticky='ns')

        self.date_label.config(font=(20))
        self.quantity_label.config(font=(20))
    
        # create instance of calc_layout class so that we can access methods (to then modify text here)
        digitPanel = calc_layout(master=self.adding_frame, width=((1000*6)/8), height=((800*6)/7), API=self.calcAPI, key1=calc_key1, placeholder_list=placeholder_list)
        digitPanel.grid(column=0, row=1, padx=25, pady=18, sticky='nsew')

      
        # buttons frame contains 2 buttons: 
        # 1) add more items? (enables for another item to be scanned and then for the process to start again)
        # 2) finish session (closes the pop-up, when all items to be added are done so)
        self.buttons = tb.Frame(self.adding_frame, width=((1000*3)/8), height=(800), border=8, relief='solid', padding=(10, 5))
        self.buttons.grid(column=1, row=1, sticky='ew', padx=(20,10))
        self.buttons.columnconfigure(0, weight=1)
        self.buttons.rowconfigure(0, weight=1)
        self.buttons.rowconfigure(1, weight=1)

        addMore = tb.Button(self.buttons, text="Add More", padding=(20, 15), bootstyle="outline-success").grid(column=0, row=0, sticky='sew')
        ## both sumbit data to table and close toplevel window

        endSession = tb.Button(self.buttons, text="Done", padding=(20, 15), bootstyle="outline-warning", command=lambda: (self.destroy(), submit_addItems(self.product_id, int(self.date.get()[:2]), int(self.date.get()[3:]), int(self.quantity.get()))))
        endSession.grid(column=0, row=1, sticky='new', pady=(15, 0))


class ItemDetails(tb.Toplevel):
    def __init__(self, top_level_frame, item_id=None, themename="superhero"):
        super().__init__(title="Register Item", size=(600, 450))
        self.columnconfigure(0, weight=1)
        self.rowconfigure((1, 2), weight=1)
        self.top_level_frame = top_level_frame
        self.item_id = item_id

        # TODO query table where it's like 'get row data where BARCODE = ONE SCANNED'
        # TODO MUST FINISH IMPLEMENTATION WHEN BARCODE SCANNING IS FUNCTIONAL. several widgets down below depend upon querying database for info, needs to be passed the actual barcode scanned!
        ## of course if there isn't an equivalent barcode within the db, then leave it unfilled

        ## top bar Menu for navigating between editor and view

        self.main_btn_frame = tb.Frame(self, relief='raised', borderwidth=10)
        self.main_btn_frame.grid(column=0, row=0, sticky='nsew')
        self.main_btn_frame.columnconfigure((0, 1), weight=1)
        self.main_btn_frame.rowconfigure(0, weight=1)

        
        check_var = BooleanVar(value=False)
        edit_btn_text = StringVar(value="Edit")

        edit_btn = tb.Checkbutton(self.main_btn_frame, textvariable=edit_btn_text, variable=check_var, bootstyle='warning-toolbutton', width=20, command=lambda: self.checkbtn_clicked(check_var, edit_btn_text))
        edit_btn.grid(column=0, row=0, sticky='e', padx=(0, 3))
        ## when selected bring up 

        finish_btn = tb.Button(self.main_btn_frame, text="Enter", width=20, bootstyle='success', command=self.finish_btn_click)
        finish_btn.grid(column=1, row=0, sticky='w', padx=(3, 0))

        self.selected_item = StringVar()
        self.selected_user = StringVar()

        ## EDIT Frame of the item details
        self.edit_details_frame = tb.Frame(self, relief='solid', borderwidth=10)
        self.edit_details_frame.grid(column=0, row=1, sticky='nsew')
        self.edit_details_frame.columnconfigure(1, weight=1)
        self.edit_details_frame.rowconfigure((0, 1), weight=1)

        # EDIT Frame widgets
        itemname_label = tb.Label(self.edit_details_frame, text="Name:")
        itemname_label.grid(column=0, row=0, sticky='e', padx=(0,5))
        itemname_label.config(font=('Arial', 14))
        itemname_entry = tb.Entry(self.edit_details_frame, textvariable=self.selected_item)
        itemname_entry.grid(column=1, row=0, sticky='ew', padx=20)
        
        itemuser_label = tb.Label(self.edit_details_frame, text='Section:')
        itemuser_label.grid(column=0, row=1, sticky='e')
        itemuser_label.config(font=('Arial', 14))
        users = get_table_data(['username'], None, 'users', False)
        itemuser_entry = tb.OptionMenu(self.edit_details_frame, self.selected_user, "select a user", *users, direction='below')
        itemuser_entry.grid(column=1, row=1, sticky='ew', padx=20)

        ## VIEW Frame of the item details
        self.view_details_frame = tb.Frame(self, relief='solid', borderwidth=10)
        self.view_details_frame.grid(column=0, row=1, sticky='nsew')
        self.view_details_frame.columnconfigure(1, weight=1)
        self.view_details_frame.rowconfigure((0, 1), weight=1)

        # VIEW Frame widgets
        itemname_label_view = tb.Label(self.view_details_frame, text="Name:")
        itemname_label_view.grid(column=0, row=0, sticky='e', padx=(0,5))
        itemname_label_view.config(font=('Arial', 14))
        itemname_entry_view = tb.Label(self.view_details_frame, textvariable=self.selected_item, relief='solid', bootstyle='light', padding=(10, 5))
        itemname_entry_view.grid(column=1, row=0, sticky='ew', padx=20)
        
        itemuser_label_view = tb.Label(self.view_details_frame, text='Section:')
        itemuser_label_view.grid(column=0, row=1, sticky='e')
        itemuser_label_view.config(font=('Arial', 14))
        itemuser_entry_view = tb.Label(self.view_details_frame, textvariable=self.selected_user, relief='solid', bootstyle="light", padding=(10, 5))
        itemuser_entry_view.grid(column=1, row=1, sticky='ew', padx=20)

        ## STATS frame for item stats 
        self.item_stats_frame = tb.Frame(self, bootstyle='warning')
        self.item_stats_frame.grid(column=0, row=2, sticky='nsew')
        self.item_stats_frame.columnconfigure((0, 1), weight=1)
        self.item_stats_frame.rowconfigure(0, weight=1)

        # implement actual querying for the collect product_id
        closest_exp_table = get_table_data(['expiry_date_month', 'expiry_date_year'], 'WHERE products.product_id = 2 ORDER BY expiry_date_month, expiry_date_year ASC LIMIT 3', 'all', True, 
                       master=self.item_stats_frame, 
                       searchable=False)
        # 2 here is the product id of the scanned product
         
        closest_exp_table.grid(column=0, row=0, sticky='nsew', rowspan=2)
        self.total_items_frame = tb.LabelFrame(self.item_stats_frame, text=" total items ", borderwidth=20)
        self.total_items_frame.grid(column=1, row=0, sticky='nsew')
        self.total_items_frame.columnconfigure(0, weight=1)
        self.total_items_frame.rowconfigure(0, weight=1)
        ## total_items_var queries the database for the total number of this particular product.
        total_items_var = StringVar(value=(get_table_data(['COUNT (*)'], 'WHERE product_id=2', 'products', False))[0][0])
        total_items_label = tb.Label(self.total_items_frame, text=(total_items_var.get()), font=('Arial',40), relief='solid', anchor='center')

        total_items_label.grid(column=0, row=0, sticky='nsew')
        

    def checkbtn_clicked(self, check_var, edit_btn_text):
        if check_var.get():
            edit_btn_text.set("Done")
            self.edit_details_frame.tkraise()
        else:
            edit_btn_text.set("Edit")
            self.view_details_frame.tkraise()

    # TODO Make a function that checks if there exists information on the product. If so, make StringVar() variables pre-filled 
    ## set frames to VIEW mode if pre-filled, else set to EDIT mode.

    def finish_btn_click(self):
        ## TODO submit infomation to db.
        add_update_item(self.selected_item.get(), self.selected_user.get())
        # if this is a new item...
        if self.item_id == None:
            # pass the new product_id to the AddItems toplevel frame
            self.top_level_frame.product_id = get_table_data(['product_id'], f'WHERE product_name = "{self.selected_item.get()}"', 'products', False)[0][0]
        ## elif self.item_id != None AND TODO (ItemDetails window has been accessed via the + (add item) button)
            ## TODO need to add some variable that tracks where the window has been accessed (e.g. a state button which can be 'Add' or 'View' state.)
        self.top_level_frame.adding_frame.tkraise()
        ## TODO else destroy
        self.destroy()
    ### def retrieve_item_data(self)
        

class AddUser(tb.Toplevel):
    def __init__(self, master, themename='superhero'):
        super().__init__(title='Add User', size=(400, 200), resizable=(False, False))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        
        username_entry_label = tb.Label(self, text="Enter the user's name:")
        username_entry_label.grid(column=0, row=0, sticky='s')
        
        self.username_entry = tb.Entry(self, bootstyle='danger')
        self.username_entry.grid(column=0, row=1, sticky='sew', padx=10)
        self.username_entry.focus()

        submit_username = tb.Button(self, text='Submit', bootstyle='primary', command=lambda: self.submit())
        submit_username.grid(column=0, row=2, sticky='n', pady=(20, 0))

        self.bind('<Return>', lambda event: submit_username.invoke())


    def submit(self):

        conn = sqlite3.connect('shop_inventory.db')
        c = conn.cursor()
        # insert into users table the new name of the new user.
        c.execute("INSERT INTO users (username) VALUES (?)", (self.username_entry.get(),))
        
        conn.commit()
        c.close()
        
        self.destroy()

class DeleteUser(tb.Toplevel):
    def __init__(self, master, themename='superhero'):
        super().__init__(title='delete User', size=(400, 500))
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)
        
        for i, user in enumerate(users_list):
            self.rowconfigure(i, weight=1)

            username_label = tb.Label(self, text=user[0], relief='solid', padding=(5, 10), bootstyle='warning')
            username_label.grid(column=0, row=i, sticky='ew', padx=(15))
            username_label.config(font=("Arial", 15))
            username_label.configure(anchor="center")

            delete_button = tb.Button(self, text='delete', padding=(0, 10), bootstyle="danger", command=lambda i=i, username=user: self.delete_user(username))
            delete_button.grid(column=1, row=i, sticky='ew', padx=10)

    def delete_user(self, username):
        ## TODO: must transfer all items under this user's name to another user (cannot delete otherwise)

        conn = sqlite3.connect("shop_inventory.db")
        c = conn.cursor()

        c.execute("DELETE FROM users WHERE username=?", (username))

        conn.commit()
        c.close()

        self.destroy()
        


