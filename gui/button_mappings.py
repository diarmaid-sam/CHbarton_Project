from tkinter import *
from tkinter import Tk
from tkinter import ttk
import ttkbootstrap as tb

class calc_layout(tb.Frame):
    def __init__(self, master, width, height):
        super().__init__(master, width=width, height=height, border=1, relief='solid', padding=(15))
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        self.master = master
        
        
        self.calc_construction()
        self.grid()

    def calc_construction(self):
        button1 = tb.Button(self, text='1', padding=(0), bootstyle="warning-outline")
        button1.grid(column=0, row=0, sticky='nsew', pady=(2), padx=(2))
        button2 = tb.Button(self, text='2', padding=(0), bootstyle="warning-outline")
        button2.grid(column=1, row=0, sticky='nsew', pady=(2), padx=(2))
        button3 = tb.Button(self, text='3', padding=(0), bootstyle="warning-outline")
        button3.grid(column=2, row=0, sticky='nsew', pady=(2), padx=(2))
        button4 = tb.Button(self, text='4', padding=(0), bootstyle="warning-outline")
        button4.grid(column=0, row=1, sticky='nsew', pady=(2), padx=(2))
        button5 = tb.Button(self, text='5', padding=(0), bootstyle="warning-outline")
        button5.grid(column=1, row=1, sticky='nsew', pady=(2), padx=(2))
        button6 = tb.Button(self, text='6', padding=(0), bootstyle="warning-outline")
        button6.grid(column=2, row=1, sticky='nsew', pady=(2), padx=(2))
        button7 = tb.Button(self, text='7', padding=(0), bootstyle="warning-outline")
        button7.grid(column=0, row=2, sticky='nsew', pady=(2), padx=(2))
        button8 = tb.Button(self, text='8', padding=(0), bootstyle="warning-outline")
        button8.grid(column=1, row=2, sticky='nsew', pady=(2), padx=(2))
        button9 = tb.Button(self, text='9', padding=(0), bootstyle="warning-outline")
        button9.grid(column=2, row=2, sticky='nsew', pady=(2), padx=(2))
        button_back = tb.Button(self, text='<-', padding=(0), bootstyle="danger-outline")
        button_back.grid(column=0, row=3, sticky='nsew', pady=(2), padx=(2))
        button0 = tb.Button(self, text='0', padding=(0), bootstyle="warning-outline")
        button0.grid(column=1, row=3, sticky='nsew', pady=(2), padx=(2))
        button_done = tb.Button(self, text='Done', padding=(0), bootstyle="success-outline")
        button_done.grid(column=2, row=3, sticky='nsew', pady=(2), padx=(2))
    