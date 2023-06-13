from ttkbootstrap.constants import *
import ttkbootstrap as tb
from tkinter import ttk


# nav bar window components
from dashboard import DashBoard
from inventory import Inventory
from users import Users
from history import History

class MainFrame(tb.Frame):
    def __init__(self, master_Window):
        super().__init__(master_Window, padding=(10))

        self.__navBar()

        # swapping frame mechanism for navbar
        self.frames = {} 

        for F in (DashBoard, Inventory, Users, History):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=1, column=0, sticky='nsew')
            
        
        self.show_frame(DashBoard)
        self.grid()
        

    # can probably keep track of which frame is opened at any given time to be able to then switch to that frame on-boot 
    def show_frame(self, cont):
        frame = self.frames[cont]
        
        frame.tkraise()

    def __navBar(self): 
        self.navBar = tb.Frame(self, border=2, padding=10, height=100, width=800)
        self.navBar.grid(column=0, row=0, sticky='ew')
        nav_dashboard = ttk.Button(self.navBar, text="Dashboard", padding=(15, 20), command=lambda:self.show_frame(DashBoard), bootstyle="outline").grid(column=0, row=0, sticky='ew')
        nav_inventory = ttk.Button(self.navBar, text="Inventory", padding=(15, 20), command=lambda:self.show_frame(Inventory), bootstyle="outline").grid(column=1, row=0, sticky='ew')
        nav_users = ttk.Button(self.navBar, text="Users", padding=(15, 20), command=lambda:self.show_frame(Users), bootstyle="outline").grid(column=2, row=0, sticky='ew')
        nav_history = ttk.Button(self.navBar, text="History", padding=(15, 20), command=lambda:self.show_frame(History), bootstyle="outline").grid(column=3, row=0, sticky='ew')

        self.navBar.columnconfigure(0, weight=1)
        self.navBar.columnconfigure(1, weight=1)
        self.navBar.columnconfigure(2, weight=1)
        self.navBar.columnconfigure(3, weight=1)   