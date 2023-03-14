from tkinter import *
from tkinter import ttk

root = Tk()
root.title("gui")

mainframe = ttk.Frame(root)
root.columnconfigure(0, weight=1)
mainframe.grid(column=0, row=0)

for i in range(1, 3):
    mainframe.rowconfigure(i, weight=2)

nav_bar = ttk.Frame(mainframe, borderwidth=2, padding=10)
nav_bar.grid(column=0, row=0, sticky=(N, S, E, W))

main_dashboard = ttk.Frame(mainframe, borderwidth=2, padding=10)
main_dashboard.grid(column=0, row=1, rowspan=3, sticky=(N, S, E, W))
main_dashboard.minsize(400, 400)

expSoon = ttk.Frame(mainframe, borderwidth=2, padding=10)
expSoon.grid(column=1, row=0, rowspan=2, sticky=(N, S, E, W))

rcntActivity = ttk.Frame(mainframe, borderwidth=2, padding=10)
rcntActivity.grid(column=1, row=2, rowspan=2, sticky=(N, S, E, W))


root.mainloop()