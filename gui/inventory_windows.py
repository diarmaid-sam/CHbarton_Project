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
        global var_placeholder
        var_placeholder = ""
        
        
        self.AddItem_frame()
        self.grid()

    # function to update the date text box
    
    def update_date(self, num, placeholder_list, date):

        # if the date entered is complete (i.e. 7 digits reached), then prevent user from entering any more
        if len(placeholder_list) == 7:
            return placeholder_list
        
        # placeholder_list here is updated before the actual Date is changed
        # placeholder_list changes the date, but doesn't permanently change (globally)
        placeholder_list += num

        # placing '/' at relevant positions when typing in the expirey date
        if len(placeholder_list) == 2:
            placeholder_list += "/"
        
        # updating the date using set method
        date.set(placeholder_list)

        return placeholder_list

        
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
        digitPanel = calc_layout(master=self.adding_frame, width=((1000*6)/8), height=((800*6)/7), function1=self.update_date, placeholder_list=[var_placeholder], f1_var1=self.date)
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
