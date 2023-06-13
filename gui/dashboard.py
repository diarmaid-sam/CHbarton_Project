import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import ttkbootstrap.tableview as tbtable
from ttkbootstrap.scrolled import ScrolledFrame

## Personal modules
from toplevel_windows import *
from db_queries import *

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
        # CALL db.queries function to get values
        self.total_items = tk.StringVar(value=item_state()) 
        self.total_shortdated = tk.StringVar(value=item_state("short"))
        self.total_expired = tk.StringVar(value=item_state("expired"))
        # the number of items indate is expressed as (TOTAL - (SHORTDATED + EXPIRED))
        self.total_indate = tk.StringVar(value=(int(self.total_items.get())-(int(self.total_shortdated.get())+int(self.total_expired.get()))))

        # create a progress bar and align vertically
        total_items_pb = tb.Progressbar(self.shop_status, orient='vertical', mode='determinate', bootstyle='success')
        # the value is equivalent to the total number of indate items (total-(shortdated+expired)) expressed as a percentage
        total_items_pb['value'] = (int(self.total_indate.get())/int(self.total_items.get())*100)
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
        

        self.lf_bottom = tb.LabelFrame(self.left_frame, text=' manage inventory ',relief='solid', bootstyle="info")
        self.lf_bottom.grid(column=0, row=1, sticky='nsew')
        self.lf_bottom.rowconfigure(0, weight=1)
        self.lf_bottom.columnconfigure(0, weight=1)
        self.lf_bottom.columnconfigure(1, weight=1)
        # top right segment of left frame (shop overview)
        
        # structure of bottom segement of left frame (manage Inventory buttons)
        lf_rmvItem = tb.Button(self.lf_bottom, text='-', padding=(30,20)).grid(column=0, row=0, padx=30, pady=30)
        lf_addItem = tb.Button(self.lf_bottom, text='+', command=lambda:AddItems(self), padding=(30,20)).grid(column=1, row=0, padx=30, pady=30)
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

        rcnt_table = get_table_data(['product_name', 'expiry_date_month', 'expiry_date_year', 'quantity', 'date_added'], None, 'all', True, master=self.rf_rcntAdded)
        rcnt_table.grid(column=0, row=0, sticky='nsew')



        self.rf_bottom = tb.LabelFrame(self.right_frame, text=' my section ',border=2, bootstyle='danger', padding=(4))
        self.rf_bottom.grid(column=0, row=1, sticky='nsew')
        self.rf_bottom.rowconfigure(0, weight=1)
        self.rf_bottom.columnconfigure(0, weight=1)
        self.rf_bottom.rowconfigure(1, weight=10)

        self.selected_staff = tk.StringVar()
        # using self.selected_staff.get you can retrieve the currently selected user. This can then be used to show the relevant section information
        # when passed into the function
        
        # table frame for 'my section' section of the dashboard
        self.my_section_table = tb.Frame(self.rf_bottom)
        self.my_section_table.grid(column=0, row=1, sticky='nsew')

        rf_selectUser = tb.OptionMenu(self.rf_bottom, self.selected_staff, 'user', *users_list, bootstyle='danger-outline')
        rf_selectUser.grid(column=0, row=0, sticky='ne')
        
        self.user_tables = {}

        for user in users_list:
            table = get_table_data(['product_name', 'expiry_date_month', 'expiry_date_year', 'quantity', 'date_added'], f'WHERE username = "{user[0]}"', 'all', True, master=self.my_section_table)
            table.grid(column=0, row=0)
            self.user_tables[user[0]] = table

        # track changes to self.selected_staff var. If changes are made (i.e. optionMenu is selected),
        self.selected_staff.trace("w", self.raise_table)

        self.grid()
        
    def raise_table(self, *args):
        self.user_tables[self.selected_staff.get()].tkraise()
        return 
    