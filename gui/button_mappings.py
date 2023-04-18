from tkinter import *
from tkinter import Tk
from tkinter import ttk
import ttkbootstrap as tb

# the class will accept a function which deals with updating a text frame when the button is clicked
class calc_layout(tb.Frame):
    # class takes functions as parameters in order to make the use of the digit keyboard in a completely flexible way. therefore implementation is flexible
    def __init__(self, master, width, height, function1, placeholder_list, f1_var1):
        super().__init__(master, width=width, height=height, border=1, relief='solid', padding=(15))
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        self.master = master
        # change date function
        self.function1 = function1
        self.placeholder_list = placeholder_list
        self.f1_var1 = f1_var1
        # place buttons into calc_layout frame
        self.calc_construction()
    
    def function1_call(self, var1, placeholder_list, f1_var1):
        placeholder_list[0] = self.function1(num=var1, placeholder_list=placeholder_list[0], date=f1_var1)
        return placeholder_list[0]
        

    def calc_construction(self):
        button1 = tb.Button(self, text='1', padding=(0), bootstyle="warning-outline", command=lambda: self.function1_call(var1="1", placeholder_list=self.placeholder_list, f1_var1=self.f1_var1))
        button1.grid(column=0, row=0, sticky='nsew', pady=(2), padx=(2))
        button2 = tb.Button(self, text='2', padding=(0), bootstyle="warning-outline", command=lambda: self.function1_call(var1="2", placeholder_list=self.placeholder_list, f1_var1=self.f1_var1))
        button2.grid(column=1, row=0, sticky='nsew', pady=(2), padx=(2))
        button3 = tb.Button(self, text='3', padding=(0), bootstyle="warning-outline", command=lambda: self.function1_call(var1="3", placeholder_list=self.placeholder_list, f1_var1=self.f1_var1))
        button3.grid(column=2, row=0, sticky='nsew', pady=(2), padx=(2))
        button4 = tb.Button(self, text='4', padding=(0), bootstyle="warning-outline", command=lambda: self.function1_call(var1="4", placeholder_list=self.placeholder_list, f1_var1=self.f1_var1))
        button4.grid(column=0, row=1, sticky='nsew', pady=(2), padx=(2))
        button5 = tb.Button(self, text='5', padding=(0), bootstyle="warning-outline", command=lambda: self.function1_call(var1="5", placeholder_list=self.placeholder_list, f1_var1=self.f1_var1))
        button5.grid(column=1, row=1, sticky='nsew', pady=(2), padx=(2))
        button6 = tb.Button(self, text='6', padding=(0), bootstyle="warning-outline", command=lambda: self.function1_call(var1="6", placeholder_list=self.placeholder_list, f1_var1=self.f1_var1))
        button6.grid(column=2, row=1, sticky='nsew', pady=(2), padx=(2))
        button7 = tb.Button(self, text='7', padding=(0), bootstyle="warning-outline", command=lambda: self.function1_call(var1="7", placeholder_list=self.placeholder_list, f1_var1=self.f1_var1))
        button7.grid(column=0, row=2, sticky='nsew', pady=(2), padx=(2))
        button8 = tb.Button(self, text='8', padding=(0), bootstyle="warning-outline", command=lambda: self.function1_call(var1="8", placeholder_list=self.placeholder_list, f1_var1=self.f1_var1))
        button8.grid(column=1, row=2, sticky='nsew', pady=(2), padx=(2))
        button9 = tb.Button(self, text='9', padding=(0), bootstyle="warning-outline", command=lambda: self.function1_call(var1="9", placeholder_list=self.placeholder_list, f1_var1=self.f1_var1))
        button9.grid(column=2, row=2, sticky='nsew', pady=(2), padx=(2))
        button_back = tb.Button(self, text='<-', padding=(0), bootstyle="danger-outline")
        button_back.grid(column=0, row=3, sticky='nsew', pady=(2), padx=(2))
        button0 = tb.Button(self, text='0', padding=(0), bootstyle="warning-outline", command=lambda: self.function1_call(var1="0", placeholder_list=self.placeholder_list, f1_var1=self.f1_var1))
        button0.grid(column=1, row=3, sticky='nsew', pady=(2), padx=(2))
        button_done = tb.Button(self, text='Done', padding=(0), bootstyle="success-outline")
        button_done.grid(column=2, row=3, sticky='nsew', pady=(2), padx=(2))
    