from tkinter import *
from tkinter import Tk
from tkinter import ttk
import ttkbootstrap as tb

class calc_layout(tb.Frame):
    def __init__(self, master):
        super.__init__(master)
        self.button_size = button_size
        self.master = master

    def calc_construction():

        button1 = tb.Button(self, text='1', width=20, padding=(0,45), bootstyle="warning-outline").grid(column=0, row=1, sticky='nsew', pady=(2), padx=(2))
        button2 = tb.Button(self, text='2', width=20, padding=(0,45), bootstyle="warning-outline").grid(column=1, row=1, sticky='nsew', pady=(2), padx=(2))
        button3 = tb.Button(self, text='3', width=20, padding=(0,45), bootstyle="warning-outline").grid(column=2, row=1, sticky='nsew', pady=(2), padx=(2))
        button4 = tb.Button(self, text='4', width=20, padding=(0,45), bootstyle="warning-outline").grid(column=0, row=2, sticky='nsew', pady=(2), padx=(2))
        button5 = tb.Button(self, text='5', width=20, padding=(0,45), bootstyle="warning-outline").grid(column=1, row=2, sticky='nsew', pady=(2), padx=(2))
        button6 = tb.Button(self, text='6', width=20, padding=(0,45), bootstyle="warning-outline").grid(column=2, row=2, sticky='nsew', pady=(2), padx=(2))
        button7 = tb.Button(self, text='7', width=20, padding=(0,45), bootstyle="warning-outline").grid(column=0, row=3, sticky='nsew', pady=(2), padx=(2))
        button8 = tb.Button(self, text='8', width=20, padding=(0,45), bootstyle="warning-outline").grid(column=1, row=3, sticky='nsew', pady=(2), padx=(2))
        button9 = tb.Button(self, text='9', width=20, padding=(0,45), bootstyle="warning-outline").grid(column=2, row=3, sticky='nsew', pady=(2), padx=(2))
        button0 = tb.Button(self, text='0', width=20, padding=(0,45), bootstyle="warning-outline").grid(column=1, row=4, sticky='nsew', pady=(2), padx=(2))
        button_back = tb.Button(self, text='<-', width=20, padding=(0,45), bootstyle="danger-outline").grid(column=0, row=4, sticky='nsew', pady=(2), padx=(2))
        button_enter = tb.Button(self, text='Done', width=20, padding=(0,45), bootstyle="success-outline").grid(column=2, row=4, sticky='nsew', pady=(2), padx=(2))
    