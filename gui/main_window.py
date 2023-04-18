import tkinter as tk
from tkinter import ttk
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledFrame
from inventory_windows import AddItems

staff = ['User', 'Cheryl', 'Sarah', 'Lauren', 'Nicola']

class DashBoard(tb.Frame):
    def __init__(self, container):
        
        super().__init__(container, border=2, height=600, width=800, bootstyle="primary")   
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        
        # left frame structure of Dashboard
        self.left_frame = tb.Frame(self, border=2, height=700, width=400)
        self.left_frame.grid(column=0, row=0, sticky='nsew')
        self.left_frame.rowconfigure(0, weight=2)
        self.left_frame.columnconfigure(0, weight=1)
        self.left_frame.columnconfigure(1, weight=1)
        # left frame segments + their structure
        self.lf_top_left = tb.Frame(self.left_frame, border=2, height=400, width=200)
        self.lf_top_left.grid(column=0, row=0, sticky='nsew')
        self.lf_top_left.rowconfigure(0, weight=1)
        self.lf_top_left.rowconfigure(1, weight=1)
        self.lf_top_left.rowconfigure(2, weight=1)

        # top left segment with the 3 meters.
        meter_total = tb.Meter(self.lf_top_left, subtext="items", metersize=150, metertype='semi', wedgesize=40).grid(column=0, row=0, sticky='nsew')
        meter_amber = tb.Meter(self.lf_top_left, subtext="short-dated", metersize=150, metertype='semi', wedgesize= 50).grid(column=0, row=1, sticky='nsew')
        meter_red = tb.Meter(self.lf_top_left, subtext="expired", metersize=150, metertype='semi', wedgesize=10).grid(column=0, row=2, sticky='nsew')

        self.lf_top_right = tb.LabelFrame(self.left_frame, text=' shop status ',border=2, height=400, width=200, bootstyle='success')
        self.lf_top_right.grid(column=1, row=0, sticky='nsew', padx=4, pady=4)

        # top right segment of left frame (shop overview)
        
        
        # bottom segment of left frame
        self.lf_bottom = tb.Frame(self.left_frame, border=2, height=200, width=400)
        self.lf_bottom.grid(column=0, row=1, sticky='nsew', columnspan=2)
        self.lf_bottom.rowconfigure(1, weight=4)
        self.lf_bottom.columnconfigure(0, weight=1)
        self.lf_bottom.columnconfigure(1, weight=1)
        self.lf_bottom.columnconfigure(2, weight=1)


        # structure of bottom segement of left frame (manage Inventory buttons)
        lf_bottom_title = tb.Label(self.lf_bottom, text="Manage Inventory", anchor='center').grid(column=1, row=0, sticky='ew')
        lf_rmvItem = tb.Button(self.lf_bottom, text='-').grid(column=0, row=1, sticky='nsew')
        lf_Inspect = tb.Button(self.lf_bottom, text='Inspect').grid(column=1, row=1, sticky='nsew')
        lf_addItem = tb.Button(self.lf_bottom, text='+', command=lambda:AddItems(self)).grid(column=2, row=1, sticky='nsew')
        self.bind("<Control-Return>", lambda event: lf_addItem.invoke())    
        

        # right frame section start
        self.right_frame = tb.Frame(self, border=2, height=700, width=400)
        self.right_frame.grid(column=1, row=0, sticky='nsew')
        self.right_frame.rowconfigure(0, weight=1)
        self.right_frame.rowconfigure(1, weight=1)
        self.right_frame.columnconfigure(0, weight=1)


        # right frame segments
        self.rf_top = tb.LabelFrame(self.right_frame, text=' recently added ', border=2, height=300, width=400, padding=(5), bootstyle='warning')
        self.rf_top.grid(column=0, row=0, sticky='nsew', padx=4, pady=4)
        self.rf_top.rowconfigure(0, weight=1)
        self.rf_top.columnconfigure(0, weight=1)
        
        # this is a 'ScrolledFrame' meaning a vertical scrollbar enables the contents of the frame to be explored (the contents will not adjust to the height)
        self.rf_rcntAdded = ScrolledFrame(self.rf_top, height=250, width=380, bootstyle='round')
        self.rf_rcntAdded.grid(column=0, row=0, sticky='nsew')


        self.rf_bottom = tb.LabelFrame(self.right_frame, text=' my section ',border=2, height=300, width=400, bootstyle='danger', padding=(4))
        self.rf_bottom.grid(column=0, row=1, sticky='nsew')
        self.rf_bottom.rowconfigure(1, weight=1)
        self.rf_bottom.columnconfigure(0, weight=1)

        self.selected_staff = tk.StringVar()
        self.selected_staff.set(staff[0])
        rf_selectUser = tb.OptionMenu(self.rf_bottom, self.selected_staff, *staff, bootstyle='danger-outline')
        rf_selectUser.grid(column=0, row=0, padx=7, sticky='e')

        self.grid()

class Inventory(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, border=2, height=600, width=800, bootstyle="primary")

        self.grid()

class Button1(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, border=2, height=600, width=800, bootstyle="primary")

        self.grid()

class Button2(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, border=2, height=600, width=800, bootstyle="primary")

        self.grid()

class Users(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, border=2, height=600, width=800, bootstyle="primary")

        self.grid()

class History(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, border=2, height=600, width=800, bootstyle="primary")

        self.grid()

class MainFrame(tb.Frame):
    def __init__(self, master_Window):
        super().__init__(master_Window, padding=(10), relief="solid", width=800, height=800)
        self.__navBar()

        self.frames = {} 

        for F in (DashBoard, Inventory, Button1, Button2, Users, History):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=1, column=0, sticky='nsew')

        self.show_frame(DashBoard)
        self.grid()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def __navBar(self): 
        self.navBar = tb.Frame(self, border=2, padding=10, height=100, width=800)
        self.navBar.grid(column=0, row=0, sticky='ew')
        nav_dashboard = ttk.Button(self.navBar, text="Dashboard", padding=(15, 20), command=lambda:self.show_frame(DashBoard), bootstyle="outline").grid(column=0, row=0, sticky='ew')
        nav_inventory = ttk.Button(self.navBar, text="Inventory", padding=(15, 20), command=lambda:self.show_frame(Inventory), bootstyle="outline").grid(column=1, row=0, sticky='ew')
        nav_button1 = ttk.Button(self.navBar, text="Button1", padding=(15, 20), command=lambda:self.show_frame(Button1), bootstyle="outline").grid(column=2, row=0, sticky='ew')
        nav_button2 = ttk.Button(self.navBar, text="Button2", padding=(15, 20), command=lambda:self.show_frame(Button2), bootstyle="outline").grid(column=3, row=0, sticky='ew')
        nav_users = ttk.Button(self.navBar, text="Users", padding=(15, 20), command=lambda:self.show_frame(Users), bootstyle="outline").grid(column=4, row=0, sticky='ew')
        nav_history = ttk.Button(self.navBar, text="History", padding=(15, 20), command=lambda:self.show_frame(History), bootstyle="outline").grid(column=5, row=0, sticky='ew')

        self.navBar.columnconfigure(0, weight=1)
        self.navBar.columnconfigure(1, weight=1)
        self.navBar.columnconfigure(2, weight=1)
        self.navBar.columnconfigure(3, weight=1)
        self.navBar.columnconfigure(4, weight=1)
        self.navBar.columnconfigure(5, weight=1)

if __name__ == "__main__":
    app = tb.Window("Software", themename="superhero", minsize=(800, 800))
    MainFrame(app)
    app.mainloop()