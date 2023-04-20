from tkinter import *
from tkinter import Tk
from tkinter import ttk
import ttkbootstrap as tb

# the class will accept a function which deals with updating a text frame when the button is clicked
class calc_layout(tb.Frame):
    # class takes functions as parameters in order to make the use of the digit keyboard in a completely flexible way. therefore implementation is flexible
    def __init__(self, master, width, height, API, key1, placeholder_list):
        super().__init__(master, width=width, height=height, border=1, relief='solid', padding=(15))
        self.API = API
        self.key1 = key1
        self.placeholder_list = placeholder_list

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        # place buttons into calc_layout frame
        self.calc_construction()
    
    def API_call(self, *args, key1, key2, placeholder_list):

        # if a number has been passed into the API call, the appropriate placeholder is updated before being passed into the imported API
        if args:
            return self.API(*args, key1=key1[0], key2=key2, placeholder_list=placeholder_list)
        
        return self.API(key1=key1[0], key2=key2, placeholder_list=placeholder_list)
        

    def calc_construction(self):
        button1 = tb.Button(self, text='1', padding=(0), bootstyle="warning-outline", command=lambda: self.API_call('1', key1=self.key1, key2="add", placeholder_list=(self.placeholder_list)))
        button1.grid(column=0, row=0, sticky='nsew', pady=(2), padx=(2))
        button2 = tb.Button(self, text='2', padding=(0), bootstyle="warning-outline", command=lambda: self.API_call('2', key1=self.key1, key2="add", placeholder_list=(self.placeholder_list)))
        button2.grid(column=1, row=0, sticky='nsew', pady=(2), padx=(2))
        button3 = tb.Button(self, text='3', padding=(0), bootstyle="warning-outline", command=lambda: self.API_call('3', key1=self.key1, key2="add", placeholder_list=(self.placeholder_list)))
        button3.grid(column=2, row=0, sticky='nsew', pady=(2), padx=(2))
        button4 = tb.Button(self, text='4', padding=(0), bootstyle="warning-outline", command=lambda: self.API_call('4', key1=self.key1, key2="add", placeholder_list=(self.placeholder_list)))
        button4.grid(column=0, row=1, sticky='nsew', pady=(2), padx=(2))
        button5 = tb.Button(self, text='5', padding=(0), bootstyle="warning-outline", command=lambda: self.API_call('5', key1=self.key1, key2="add", placeholder_list=(self.placeholder_list)))
        button5.grid(column=1, row=1, sticky='nsew', pady=(2), padx=(2))
        button6 = tb.Button(self, text='6', padding=(0), bootstyle="warning-outline", command=lambda: self.API_call('6', key1=self.key1, key2="add", placeholder_list=(self.placeholder_list)))
        button6.grid(column=2, row=1, sticky='nsew', pady=(2), padx=(2))
        button7 = tb.Button(self, text='7', padding=(0), bootstyle="warning-outline", command=lambda: self.API_call('7', key1=self.key1, key2="add", placeholder_list=(self.placeholder_list)))
        button7.grid(column=0, row=2, sticky='nsew', pady=(2), padx=(2))
        button8 = tb.Button(self, text='8', padding=(0), bootstyle="warning-outline", command=lambda: self.API_call('8', key1=self.key1, key2="add", placeholder_list=(self.placeholder_list)))
        button8.grid(column=1, row=2, sticky='nsew', pady=(2), padx=(2))
        button9 = tb.Button(self, text='9', padding=(0), bootstyle="warning-outline", command=lambda: self.API_call('9', key1=self.key1, key2="add", placeholder_list=(self.placeholder_list)))
        button9.grid(column=2, row=2, sticky='nsew', pady=(2), padx=(2))
        button_back = tb.Button(self, text='<-', padding=(0), bootstyle="danger-outline", command=lambda: self.API_call(key1=self.key1, key2="back", placeholder_list=self.placeholder_list))
        button_back.grid(column=0, row=3, sticky='nsew', pady=(2), padx=(2))
        button0 = tb.Button(self, text='0', padding=(0), bootstyle="warning-outline", command=lambda: self.API_call('0', key1=self.key1, key2="add", placeholder_list=(self.placeholder_list)))
        button0.grid(column=1, row=3, sticky='nsew', pady=(2), padx=(2))
        button_done = tb.Button(self, text='Done', padding=(0), bootstyle="success-outline", command=lambda: self.API_call(key1=self.key1, key2="done", placeholder_list=self.placeholder_list))
        button_done.grid(column=2, row=3, sticky='nsew', pady=(2), padx=(2))
    