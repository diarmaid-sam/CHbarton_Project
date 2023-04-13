from tkinter import *
from tkinter import Tk
from tkinter import ttk
import ttkbootstrap as tb

# what is necessary:
# scan item - If the barcode is registered in the database, then the fields are automatically filled. If the barcode isn't registered, then the 'register product' comes up.
# Quantity - The number of products (make it like a calculator, with big buttons for input)
# Expiry date 

class AddItems(tb.Toplevel):
    def __init__(self, master, themename="superhero"):
        super().__init__(title="Add Items", size=(1000, 600), resizable=(False, False))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.AddItem_frame()
        self.grid()
        
    # This frame is the one where (once the item type is confirmed) the item's quantity and expiry date are inputted and put into the database
    def AddItem_frame(self):
        self.adding_frame = tb.Frame(self, width=1000, height=600, relief='raised')
        self.adding_frame.grid(column=0, row=0, sticky='nsew')
        self.adding_frame.columnconfigure(0, weight=3)
        self.adding_frame.columnconfigure(1, weight=3)
        self.adding_frame.columnconfigure(2, weight=2)
        self.expDate_frame = tb.Frame(self.adding_frame, width=250, height=800, border=2, relief='solid', padding=(10, 10, 10, 0))
        self.expDate_frame.grid(column=0, row=0, sticky='nsew')
        self.expDate_frame.columnconfigure(0, weight=1)
        self.expDate_frame.columnconfigure(1, weight=1)
        self.expDate_frame.columnconfigure(2, weight=1)
        self.date_display = tb.Frame(self.expDate_frame, width=250, height=100, border=2, relief='solid', padding=(5))
        self.date_display.grid(column=0, row=0, columnspan=3, sticky='nsew', pady=(0, 10))
        exp_button1 = tb.Button(self.expDate_frame,text='1', width=20, padding=(0,45), bootstyle="warning-outline").grid(column=0, row=1, sticky='nsew', pady=(2), padx=(2))
        exp_button2 = tb.Button(self.expDate_frame,text='2', width=20, padding=(0,45), bootstyle="warning-outline").grid(column=1, row=1, sticky='nsew', pady=(2), padx=(2))
        exp_button3 = tb.Button(self.expDate_frame,text='3', width=20, padding=(0,45), bootstyle="warning-outline").grid(column=2, row=1, sticky='nsew', pady=(2), padx=(2))
        exp_button4 = tb.Button(self.expDate_frame,text='4', width=20, padding=(0,45), bootstyle="warning-outline").grid(column=0, row=2, sticky='nsew', pady=(2), padx=(2))
        exp_button5 = tb.Button(self.expDate_frame,text='5', width=20, padding=(0,45), bootstyle="warning-outline").grid(column=1, row=2, sticky='nsew', pady=(2), padx=(2))
        exp_button6 = tb.Button(self.expDate_frame,text='6', width=20, padding=(0,45), bootstyle="warning-outline").grid(column=2, row=2, sticky='nsew', pady=(2), padx=(2))
        exp_button7 = tb.Button(self.expDate_frame,text='7', width=20, padding=(0,45), bootstyle="warning-outline").grid(column=0, row=3, sticky='nsew', pady=(2), padx=(2))
        exp_button8 = tb.Button(self.expDate_frame,text='8', width=20, padding=(0,45), bootstyle="warning-outline").grid(column=1, row=3, sticky='nsew', pady=(2), padx=(2))
        exp_button9 = tb.Button(self.expDate_frame,text='9', width=20, padding=(0,45), bootstyle="warning-outline").grid(column=2, row=3, sticky='nsew', pady=(2), padx=(2))
        exp_button0 = tb.Button(self.expDate_frame,text='0', width=20, padding=(0,45), bootstyle="warning-outline").grid(column=1, row=4, sticky='nsew', pady=(2), padx=(2))
        exp_button_back = tb.Button(self.expDate_frame,text='<-', width=20, padding=(0,45), bootstyle="danger-outline").grid(column=0, row=4, sticky='nsew', pady=(2), padx=(2))
        exp_button_enter = tb.Button(self.expDate_frame,text='Done', width=20, padding=(0,45), bootstyle="success-outline").grid(column=2, row=4, sticky='nsew', pady=(2), padx=(2))




        self.quantity_frame = tb.Frame(self.adding_frame, width=250, height=800, border=2, relief='solid', padding=(10, 5))
        self.quantity_frame.grid(column=1, row=0, sticky='nsew')

        # buttons frame contains 2 buttons: 
        # 1) add more items? (enables for another item to be scanned and then for the process to start again)
        # 2) finish session (closes the pop-up, when all items to be added are done so)
        self.buttons = tb.Frame(self.adding_frame, width=100, height=800, border=2, padding=(10, 5))
        self.buttons.grid(column=2, row=0, sticky='nsew')
        self.buttons.rowconfigure(0, weight=1)
        self.buttons.rowconfigure(1, weight=1)

        addMore = tb.Button(self.buttons, text="Add More", padding=(10, 5), bootstyle="success").grid(column=0,row=0, sticky='ew')
        endSession = tb.Button(self.buttons, text="Done", padding=(10, 5), bootstyle="warning", command=lambda: self.destroy()).grid(column=0, row=1, sticky='n')
