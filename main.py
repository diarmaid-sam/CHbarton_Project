import sqlite3
from tkinter import *

root = Tk()
root.title("gui")
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()