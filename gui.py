#!/usr/bin/env python
# import pandas as pd
# import numpy as np
from tkinter import *

# Create GUI
root = tk.Tk()
canvas1 = tk.Canvas(root, width = 500, height = 300)
canvas1.pack()

# create entry fields
label1 = tk.Entry(root, text='Total Options Granted: ')
canvas1.create_window(100, 60, window=label1)
entry1 = tk.Entry(root)
canvas1.create_window(300, 60, window=entry1)

label2 = tk.Label(root, text='Vesting Start Date: ')
canvas1.create_window(100, 80, window=label2)
# entry2 = tk.Entry(root)
# canvas1.create_window(300, 80, window=entry2)
sel=tk.StringVar() # declaring string variable
cal1=DateEntry(root, selectmode='day', textvariable=sel)
cal1.grid(row=1,column=1,padx=20)
def my_upd(*args):
    l1.config(text=sel.get())

l1=tk.Lable(root, bg='yellow') # label to display date
l1.grid(row=1, column=2)

sel.trace('w',my_upd)
root.mainloop()


# label3 = tk.Label(root, text='Vesting End Date: ')
# canvas1.create_window(100, 60, window=label3)
# entry3 = tk.Entry(root)
# canvas1.create_window(300, 60, window=entry3)

# create function to be used as button command
def values():
    global total_options
    total_options = (entry1.get())

    global vesting_start