import tkinter.font as tkfont
from tkinter import ttk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

## Personal modules
from toplevel_windows import *
from db_queries import *

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
        add_user_button = tb.Button(self.manage_users_frame, text='add users', padding=(0, 10), bootstyle='outline-success', command= lambda:AddUser(self))
        add_user_button.grid(column=0, row=0, sticky='nsew', padx=5, pady=5)
        # TODO change name for user.
        edit_user_button = tb.Button(self.manage_users_frame, text='edit users', padding=(0, 10), bootstyle='outline')
        edit_user_button.grid(column=1, row=0, sticky='nsew', padx=(0, 5), pady=5)
        remove_user_button = tb.Button(self.manage_users_frame, text='remove users', padding=(0, 10), bootstyle='outline-danger', command= lambda:DeleteUser(self, app))
        remove_user_button.grid(column=2, row=0, sticky='nsew', padx=(0, 5), pady=5)

        # new frame for user associated buttons (variable number)
        self.user_list_frame = tb.Frame(self.user_lf, borderwidth=30, relief='solid')
        self.user_list_frame.grid(column=0, row=2, sticky='nsew', padx=5, pady=5)
        self.user_list_frame.columnconfigure(0, weight=1)

        notebooks = []
        for i, user in enumerate(users_list):
            # get user_id 
            stringggg = 'WHERE username = diarmaid'
            user_id = get_table_data(['user_id'], f'WHERE username = "{user[0]}"', 'users', False)

            #creating right frame notebooks 
            notebook = tb.Notebook(self.user_rf)


            frame1 = tb.Frame(notebook, bootstyle='dark')
            frame1.grid(column=0, row=0, sticky='nsew')
            frame1.columnconfigure(0, weight=1)
            frame1.rowconfigure(0, weight=1)
            
            user_section_table = get_table_data(['product_name', 'expiry_date_month', 'expiry_date_year', 'quantity', 'date_added'], f'WHERE users.user_id = {user_id[0][0]}', 'all', True, master=frame1, searchable=True)
            user_section_table.grid(column=0, row=0, sticky='nsew')
            notebook.add(frame1, text=user[0] + "'s section")

            frame2_table_query = f"WHERE user_id = {user_id[0][0]}"

            frame2 = tb.Frame(notebook, bootstyle='light')
            frame2.grid(column=0, row=0, sticky='nsew')
            frame2.columnconfigure(0, weight=1)
            frame2.rowconfigure(0, weight=1)
            user_items_table = get_table_data(['product_name'], frame2_table_query, 'products', True, master=frame2, searchable=True)
            user_items_table.grid(column=0, row=0, sticky='nsew')

            notebook.add(frame2, text=user[0] + "'s items")

            notebook.grid(column=0, row=0, sticky='nsew')
            notebooks.append(notebook)
            


            ## CONSTRUCT LEFT FRAME BUTTONS
            user_button = tb.Button(self.user_list_frame, text=user, padding=(0, 5), bootstyle='outline-primary', command=lambda i=i: notebooks[i].tkraise())
            user_button.grid(column=0, row=i, sticky='nsew', padx=5, pady=10)
            self.user_list_frame.rowconfigure(i, weight=1)

        self.grid()