import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import ttkbootstrap.tableview as tbtable
from ttkbootstrap.scrolled import ScrolledFrame

## Personal modules
from toplevel_windows import *
from db_queries import *

class Inventory(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, height=600, width=800)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # top frame for navigation of the inventory table
        self.inventory_top_frame = tb.Frame(self)
        self.inventory_top_frame.grid(column=0, row=0, sticky='new', pady=(10, 15))
        self.inventory_top_frame.columnconfigure(0, weight=12)
        self.inventory_top_frame.columnconfigure(1, weight=2)
        self.inventory_top_frame.columnconfigure(2, weight=4)
        self.inventory_top_frame.rowconfigure(0, weight=1)
        
        # widgets (entry and buttons) for the search bar
        inventory_title = tb.Label(self.inventory_top_frame, text="S h o p    I n v e n t o r y", bootstyle='light', padding=10)
        inventory_title.grid(column=0, row=0, sticky='ew')
        
        # configuring the style of inventory_title label. this code snippet underlines and increases text size to 20
        my_font = tkfont.Font(inventory_title, inventory_title.cget("font"))
        my_font.configure(underline=True)
        my_font.configure(size=(20))

        inventory_title.config(font=(my_font))
        

        inventory_filter_by = tb.Menubutton(self.inventory_top_frame, text='Filter By', padding=(4, 10, 0, 10), bootstyle='outline-warning')
        inventory_filter_by.grid(column=1, row=0, sticky='ew')

        # add item button of the utility frame
        add_button = tb.Button(self.inventory_top_frame, text="Add", padding=(0, 10), command=lambda:AddItems(self), bootstyle='outline-success')
        add_button.grid(column=2, row=0, sticky='ew', padx=(10))

        separator = tb.Separator(self.inventory_top_frame, bootstyle='light') 
        separator.grid(column=0, row=1, sticky='nsew', columnspan=3, pady=(10,0))

        inventory_table = get_table_data(['product_name', 'expiry_date_month', 'expiry_date_year', 'quantity', 'username', 'date_added'], None, 'all', True, master=self, searchable='true', state='view')
        inventory_table.grid(column=0, row=1, sticky='nsew')

        self.grid()