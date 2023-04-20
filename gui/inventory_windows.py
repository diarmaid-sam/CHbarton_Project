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
        self.rowconfigure(0, weight=1)  
        global placeholder_list
        global calc_key1
        # lists are necessary as updating values using int or str data_types causes issues
        placeholder_list = ['', '']
        calc_key1 = [0]
        
        
        self.AddItem_frame()
        self.grid()

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
                return# TODO: probably pass the date and quantity info into the database
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

        self.date_label = tb.Label(self.input_display, textvariable=self.date, border=1, relief='solid', padding=10)
        self.date_label.grid(column=0, row=0, sticky='nsew', pady=5, padx=5)
        self.quantity_label = tb.Label(self.input_display, textvariable=self.quantity, border=1, relief='solid', padding=10)
        self.quantity_label.grid(column=0, row=1, sticky='nsew', pady=(0, 5), padx=5)
    
        
        # create instance of calc_layout class so that we can access methods (to then modify text here)
        digitPanel = calc_layout(master=self.adding_frame, width=((1000*6)/8), height=((800*6)/7), API=self.calcAPI, key1=calc_key1, placeholder_list=placeholder_list)
        digitPanel.grid(column=0, row=1, padx=25, pady=18, sticky='nsew')

      
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
