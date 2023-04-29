import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import ttkbootstrap.tableview as tbtable
from ttkbootstrap.scrolled import ScrolledFrame
from toplevel_windows import AddItems

staff = ['Cheryl', 'Sarah', 'Lauren', 'Nicola']

# TODO design a function to show relevant table information associated with given staff member

def get_table_data(**kwargs):
    return

class DashBoard(tb.Frame):
    def __init__(self, container):
        
        super().__init__(container, border=2, height=600, width=800, bootstyle="primary")   
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        
        # left frame structure of Dashboard
        self.left_frame = tb.Frame(self, border=2, height=700, width=400)
        self.left_frame.grid(column=0, row=0, sticky='nsew')
        self.left_frame.rowconfigure(0, weight=1)
        self.left_frame.rowconfigure(1, weight=1)
        self.left_frame.columnconfigure(0, weight=1)
        # left frame segments + their structure
        self.lf_top = tb.Frame(self.left_frame)
        self.lf_top.grid(column=0, row=0, sticky='nsew')
        self.lf_top.rowconfigure(1, weight=1)
        self.lf_top.columnconfigure(0, weight=1)


        # widgets of left frame, top window
        shop_status_label = tb.Label(self.lf_top, text="s h o p  s t a t u s", padding=10, bootstyle='light')
        shop_status_label.grid(column=0, row=0, sticky='n')

        # shop label font config:
        my_font = tkfont.Font(shop_status_label, shop_status_label.cget("font"))
        my_font.configure(underline=True)
        my_font.configure(size=(20))

        shop_status_label.config(font=my_font)

        # shop progress bar frame 
        self.shop_status = tb.Frame(self.lf_top, padding=10, relief='solid')
        self.shop_status.grid(column=0, row=1, sticky='nsew', padx=10, pady=(0, 5))
        self.shop_status.rowconfigure(1, weight=1)
        self.shop_status.columnconfigure(3, weight=1)

        # variables to keep track of the actual value of total items, total items that are short-dated, and total expired items
        # TODO query database to get realtime data for these labels
        self.total_items = tk.StringVar(value="17")
        self.total_shortdated = tk.StringVar(value="6")
        self.total_expired = tk.StringVar(value="2")
        # the number of items indate is expressed as (TOTAL - (SHORTDATED + EXPIRED))
        self.total_indate = tk.StringVar(value=(int(self.total_items.get())-(int(self.total_shortdated.get())+int(self.total_expired.get()))))

        # create a progress bar and align vertically
        total_items_pb = tb.Progressbar(self.shop_status, orient='vertical', mode='determinate', bootstyle='success')
        # the value is equivalent to the total number of indate items (total-(shortdated+expired)) expressed as a percentage
        total_items_pb['value'] = ((int(self.total_items.get())-(int(self.total_shortdated.get())+int(self.total_expired.get())))/int(self.total_items.get())*100)
        total_items_pb.grid(column=0, row=0, sticky='ns', padx=(0, 12), rowspan=2)

        items_shortdated_pb = tb.Progressbar(self.shop_status, orient='vertical', mode='determinate', bootstyle='warning')
        # value is total number of shortdated items relative to total number of items, expressed as a percentage
        items_shortdated_pb['value'] = ((int(self.total_shortdated.get())/int(self.total_items.get()))*100)
        items_shortdated_pb.grid(column=1, row=0, sticky='ns', padx=(0, 12), rowspan=2)

        items_expired_pb = tb.Progressbar(self.shop_status, orient='vertical', mode='determinate', bootstyle='danger')
        items_expired_pb['value'] = ((int(self.total_expired.get())/int(self.total_items.get()))*100)
        items_expired_pb.grid(column=2, row=0, sticky='ns', padx=(0, 12), rowspan=2)


        # frame to hold labels for the shop status
        self.shop_stat_label_frame = tb.Frame(self.shop_status, relief='solid')
        self.shop_stat_label_frame.grid(column=3, row=1, sticky='new')
        # column 2 gets weight=1 so that buttons can be placed at rhs of text
        self.shop_stat_label_frame.columnconfigure(2, weight=1)
        
        
        # title label for the status of the shop
        top_label_shop_status = tb.Label(self.shop_status, text="s t a t s :", padding=10)
        top_label_shop_status.grid(column=3, row=0, sticky='nw')
        top_label_shop_status.config(font=('default', 15))

         

        total_items_label = tb.Label(self.shop_stat_label_frame, text=("ITEMS IN-DATE: "), padding=10)
        total_items_label.grid(column=0, row=1, sticky='nsew')
        total_items_label_var = tb.Label(self.shop_stat_label_frame, textvariable=self.total_indate, bootstyle="success")
        total_items_label_var.grid(column=1, row=1, sticky='nsew')

        total_items_label.config(font=("default", 13))
        total_items_label_var.config(font=("default", 15))

        total_shortdated_label = tb.Label(self.shop_stat_label_frame, text=("SHORTDATED TOTAL: "), padding=10)
        total_shortdated_label.grid(column=0, row=2, sticky='nsew')
        total_shortdated_label_var = tb.Label(self.shop_stat_label_frame, textvariable=self.total_shortdated, bootstyle="warning")
        total_shortdated_label_var.grid(column=1, row=2, sticky='nsew')

        total_shortdated_label.config(font=("default", 13))
        total_shortdated_label_var.config(font=("default", 15))

        total_expired_label = tb.Label(self.shop_stat_label_frame, text=("EXPIRED TOTAL: "), padding=10)
        total_expired_label.grid(column=0, row=3, sticky='nsew')
        total_expired_label_var = tb.Label(self.shop_stat_label_frame, textvariable=self.total_expired, bootstyle="danger")
        total_expired_label_var.grid(column=1, row=3, sticky='nsew')

        total_expired_label.config(font=("default", 13))
        total_expired_label_var.config(font=("default", 15))

        # inspect buttons for expired and shortdated items
        # TODO make functional

        shortdate_inspect_btn = tb.Button(self.shop_stat_label_frame, text='inspect', padding=3, bootstyle='outline-secondary')
        shortdate_inspect_btn.grid(column=2, row=2, sticky='e', padx=(0, 10))

    
        expired_inspect_btn = tb.Button(self.shop_stat_label_frame, text='inspect', padding=3, bootstyle='outline-secondary')
        expired_inspect_btn.grid(column=2, row=3, sticky='e', padx=(0, 10))

        


        

        self.lf_bottom = tb.Frame(self.left_frame, relief='solid')
        self.lf_bottom.grid(column=0, row=1, sticky='nsew')
        self.lf_bottom.rowconfigure(1, weight=4)
        self.lf_bottom.columnconfigure(0, weight=1)
        self.lf_bottom.columnconfigure(1, weight=1)
        self.lf_bottom.columnconfigure(2, weight=1)
        # top right segment of left frame (shop overview)
        
        
        

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
        self.rf_top = tb.LabelFrame(self.right_frame, text=' recently added ', border=2, padding=(5), bootstyle='warning')
        self.rf_top.grid(column=0, row=0, sticky='nsew', padx=4, pady=4)
        self.rf_top.rowconfigure(0, weight=1)
        self.rf_top.columnconfigure(0, weight=1)
        
        # this is a 'ScrolledFrame' meaning a vertical scrollbar enables the contents of the frame to be explored (the contents will not adjust to the height)
        self.rf_rcntAdded = ScrolledFrame(self.rf_top, bootstyle='round', autohide='true')
        self.rf_rcntAdded.grid(column=0, row=0, sticky='nsew')
        self.rf_rcntAdded.rowconfigure(0, weight=1)
        self.rf_rcntAdded.columnconfigure(0, weight=1)


        self.rf_bottom = tb.LabelFrame(self.right_frame, text=' my section ',border=2, bootstyle='danger', padding=(4))
        self.rf_bottom.grid(column=0, row=1, sticky='nsew')
        self.rf_bottom.rowconfigure(0, weight=1)
        self.rf_bottom.columnconfigure(0, weight=1)
        self.rf_bottom.rowconfigure(1, weight=10)

        self.selected_staff = tk.StringVar()
        # using self.selected_staff.get you can retrieve the currently selected user. This can then be used to show the relevant section information
        # when passed into the function
        self.selected_staff.set(staff[0])
        rf_selectUser = tb.OptionMenu(self.rf_bottom, self.selected_staff, *staff, bootstyle='danger-outline')
        rf_selectUser.grid(column=0, row=0, padx=7, sticky='ne')

        # table frame for 'my section' section of the dashboard
        self.my_section_table = tb.Frame(self.rf_bottom, border=2, relief='solid', padding=10)
        self.my_section_table.grid(column=0, row=1, sticky='nsew')
        temp_label = tb.Label(self.my_section_table, text="im a label")
        temp_label.grid(column=0, row=0, sticky='nsew')


        self.grid()

class Inventory(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, height=600, width=800)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # top frame for navigation of the inventory table
        self.inventory_top_frame = tb.Frame(self)
        self.inventory_top_frame.grid(column=0, row=0, sticky='new', pady=(10, 15))
        self.inventory_top_frame.columnconfigure(0, weight=12)
        self.inventory_top_frame.columnconfigure(1, weight=2)
        self.inventory_top_frame.columnconfigure(2, weight=4)
        self.inventory_top_frame.rowconfigure(0, weight=1)
        
        # widgets (entry and buttons) for the search bar
        inventory_title = tb.Label(self.inventory_top_frame, text="S h o p    I n v e n t o r y", bootstyle='light', padding=10)
        inventory_title.grid(column=0, row=0, sticky='ew')
        
        # configuring the style of inventory_title label. this code snippet underlines and increases text size to 20
        my_font = tkfont.Font(inventory_title, inventory_title.cget("font"))
        my_font.configure(underline=True)
        my_font.configure(size=(20))

        inventory_title.config(font=(my_font))
        

        inventory_filter_by = tb.Menubutton(self.inventory_top_frame, text='Filter By', padding=(4, 10, 0, 10), bootstyle='outline-warning')
        inventory_filter_by.grid(column=1, row=0, sticky='ew')

        # add item button of the utility frame
        add_button = tb.Button(self.inventory_top_frame, text="Add", padding=(0, 10), command=lambda:AddItems(self), bootstyle='outline-success')
        add_button.grid(column=2, row=0, sticky='ew', padx=(10))

        separator = tb.Separator(self.inventory_top_frame, bootstyle='light')
        separator.grid(column=0, row=1, sticky='nsew', columnspan=3, pady=(10,0))

        # table of entire shop_inventory.db
        # column headers for table
        coldata = [
                   {"text": "Product name", "stretch": "false"}, 
                   {"text": "expiry date", "stretch": "false"}, 
                   {"text": "quantity", "stretch": "false"},
                   {"text": "user section", "stretch": "false"},
                   {"text": "time added", "stretch": "false"}
                   ]
        
        # TODO: row data for table. Currently filled with placeholder values (import from shop_inventory.db database)
        rowdata = [
            ('A123', 'IzzyCo', 12, 'delta', 'dieeye'),
            ('A136', 'Kimdee Inc.', 45, 'delta', 'dieeye'),
            ('A158', 'Farmadding Co.', 36, 'delta', 'dieeye'),
            ('A123', 'IzzyCo', 12, 'delta', 'dieeye'),
            ('A136', 'Kimdee Inc.', 45, 'delta', 'dieeye'),
            ('A158', 'Farmadding Co.', 36, 'delta', 'dieeye')
        ]
        self.inventory_table = tbtable.Tableview(master=self,
                                                 coldata=coldata,
                                                 rowdata=rowdata,
                                                 searchable='true',
                                                 stripecolor=('gray', 'white')
                                                      )
        self.inventory_table.grid(column=0, row=1, sticky='nsew')

        self.grid()

class Users(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, border=2, height=600, width=800)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)

        # left and right frames of the mainframe (of users)
        self.user_lf = tb.Frame(self)
        self.user_lf.grid(column=0, row=0, sticky='nsew', padx=(5, 0), pady=5)

        self.user_lf.rowconfigure(2, weight=1)
        self.user_lf.columnconfigure(0, weight=1)

        self.user_rf = tb.Frame(self, borderwidth=5)
        self.user_rf.grid(column=1, row=0, sticky='nsew', padx=5, pady=5)

        self.user_rf.columnconfigure(0, weight=1)
        self.user_rf.rowconfigure(0, weight=1)

        ### LEFT FRAME  STRUCTURE ###

        # left frame structure
        lf_title_label = tb.Label(self.user_lf, text="U S E R S", padding=10, bootstyle='light')
        lf_title_label.grid(column=0, row=0, sticky='new', padx=5, pady=5)

        # styling the title label (underline)
        lf_title_font = tkfont.Font(lf_title_label, lf_title_label.cget("font"))
        lf_title_font.configure(size=(15))
        lf_title_font.configure(underline=True)
        lf_title_label.config(font=lf_title_font)
        
        # manage users frame and structure
        self.manage_users_frame = tb.LabelFrame(self.user_lf, text=" manage users ", relief='solid', bootstyle='primary', padding=(0, 0, 0, 5))
        self.manage_users_frame.grid(column=0, row=1, sticky='new')
        self.manage_users_frame.columnconfigure(0, weight=1)
        self.manage_users_frame.columnconfigure(1, weight=1)
        self.manage_users_frame.columnconfigure(2, weight=1)

        # manage_users_frame widgets
        # TODO make these buttons functional (create toplevel window)
        add_user_button = tb.Button(self.manage_users_frame, text='add users', padding=(0, 10), bootstyle='outline-success')
        add_user_button.grid(column=0, row=0, sticky='nsew', padx=5, pady=5)
        edit_user_button = tb.Button(self.manage_users_frame, text='edit users', padding=(0, 10), bootstyle='outline')
        edit_user_button.grid(column=1, row=0, sticky='nsew', padx=(0, 5), pady=5)
        remove_user_button = tb.Button(self.manage_users_frame, text='remove users', padding=(0, 10), bootstyle='outline-danger')
        remove_user_button.grid(column=2, row=0, sticky='nsew', padx=(0, 5), pady=5)

        # new frame for user associated buttons (variable number)
        self.user_list_frame = tb.Frame(self.user_lf, borderwidth=30, relief='solid')
        self.user_list_frame.grid(column=0, row=2, sticky='nsew', padx=5, pady=5)
        self.user_list_frame.columnconfigure(0, weight=1)

        notebooks = []
        for i, user in enumerate(staff):
            

            #creating right frame notebooks 
            notebook = tb.Notebook(self.user_rf)
            

            frame1 = tb.Frame(notebook, bootstyle='dark')
            frame1.grid(column=0, row=0, sticky='nsew')
            frame1.columnconfigure(0, weight=1)
            frame1.rowconfigure(0, weight=1)
            user_section_table = tbtable.Tableview(master=frame1, searchable='true')
            user_section_table.grid(column=0, row=0, sticky='nsew')
            notebook.add(frame1, text=user + "'s section")

            frame2 = tb.Frame(notebook, bootstyle='light')
            frame2.grid(column=0, row=0, sticky='nsew')
            frame2.columnconfigure(0, weight=1)
            frame2.rowconfigure(0, weight=1)
            user_items_table = tbtable.Tableview(master=frame2, searchable='true')
            user_items_table.grid(column=0, row=0, sticky='nsew')

            notebook.add(frame2, text=user + "'s items")

            notebook.grid(column=0, row=0, sticky='nsew')
            notebooks.append(notebook)
            


            ## CONSTRUCT LEFT FRAME BUTTONS
            user_button = tb.Button(self.user_list_frame, text=user, padding=(0, 5), bootstyle='outline-primary', command=lambda i=i: notebooks[i].tkraise())
            user_button.grid(column=0, row=i, sticky='nsew', padx=5, pady=10)
            self.user_list_frame.rowconfigure(i, weight=1)

            ## CONSTRUCT RIGHT FRAME NOTEBOOKS


        
        



            ##

        ### RIGHT FRAME STRUCTURE ###







        self.grid()

class History(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, border=2, height=600, width=800, bootstyle="primary")

        self.grid()

class MainFrame(tb.Frame):
    def __init__(self, master_Window):
        super().__init__(master_Window, padding=(10), relief="solid", width=800, height=800)

        self.__navBar()

        # swapping frame mechanism for navbar
        self.frames = {} 

        for F in (DashBoard, Inventory, Users, History):
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
        nav_users = ttk.Button(self.navBar, text="Users", padding=(15, 20), command=lambda:self.show_frame(Users), bootstyle="outline").grid(column=2, row=0, sticky='ew')
        nav_history = ttk.Button(self.navBar, text="History", padding=(15, 20), command=lambda:self.show_frame(History), bootstyle="outline").grid(column=3, row=0, sticky='ew')

        self.navBar.columnconfigure(0, weight=1)
        self.navBar.columnconfigure(1, weight=1)
        self.navBar.columnconfigure(2, weight=1)
        self.navBar.columnconfigure(3, weight=1)


if __name__ == "__main__":
    app = tb.Window("Software", themename="superhero", minsize=(800, 800))
    MainFrame(app)
    app.mainloop()  