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

class History(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, border=2, height=600, width=800, bootstyle="primary")

        self.grid()