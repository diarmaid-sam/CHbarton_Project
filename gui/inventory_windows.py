from tkinter import *
from tkinter import Tk
from tkinter import ttk
import ttkbootstrap as tb
from button_mappings import calc_layout

# what is necessary:
# scan item - If the barcode is registered in the database, then the fields are automatically filled. If the barcode isn't registered, then the 'register product' comes up.
# Quantity - The number of products (make it like a calculator, with big buttons for input)
# Expiry date 

class AddItems(tb.Toplevel):
    def __init__(self, master, themename="superhero"):
        super().__init__(title="Add Items", size=(1000, 800), resizable=(False, True))
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)  

        self.AddItem_frame()
        self.grid()
        
    # This frame is the one where (once the item type is confirmed) the item's quantity and expiry date are inputted and put into the database
    def AddItem_frame(self):
        self.adding_frame = tb.Frame(self, width=1000, height=800)
        self.adding_frame.grid(column=0, row=0, sticky='nsew')
        self.adding_frame.columnconfigure(0, weight=6)
        self.adding_frame.columnconfigure(1, weight=2)
        self.adding_frame.rowconfigure(0, weight=1)
        self.adding_frame.rowconfigure(1, weight=7)

        self.input_display = tb.Frame(self.adding_frame, width=((1000*6)/8), height=(800/7), relief='solid')
        self.input_display.columnconfigure(0, weight=1)
        self.input_display.grid(column=0, row=0, sticky='nsew', padx=10, pady=15)
        
        calc_layout(master=self.adding_frame, width=((1000*6)/8), height=((800*6)/7)).grid(column=0, row=1, padx=25, pady=18, sticky='nsew')


      
        # buttons frame contains 2 buttons: 
        # 1) add more items? (enables for another item to be scanned and then for the process to start again)
        # 2) finish session (closes the pop-up, when all items to be added are done so)
        self.buttons = tb.Frame(self.adding_frame, width=((1000*3)/8), height=(800), border=8, relief='solid', padding=(10, 5))
        self.buttons.grid(column=1, row=1, sticky='ew', padx=(20,0))
        self.buttons.columnconfigure(0, weight=1)
        self.buttons.rowconfigure(0, weight=1)
        self.buttons.rowconfigure(1, weight=1)

        addMore = tb.Button(self.buttons, text="Add More", padding=(20, 15), bootstyle="outline-success").grid(column=0, row=0, sticky='sew')
        endSession = tb.Button(self.buttons, text="Done", padding=(20, 15), bootstyle="outline-warning", command=lambda: self.destroy()).grid(column=0, row=1, sticky='new', pady=(15, 0))
