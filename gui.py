#!/usr/bin/env python
# import pandas as pd
# import numpy as np
from tkinter import *
# import tkinter as tk
from tkcalendar import DateEntry
from datetime import datetime

# Create GUI
root = Tk()
# Add Title
root.title("Amanda's Stock Vesting Calculator")
# Add Geometry
root.geometry("500x300")
# canvas1 = tk.Canvas(root, width = 500, height = 300)
# canvas1.pack()

# Create Total Options Granted field
label1 = Label(root, text='Total Options Granted: ').grid(row=0, column=0)
# canvas1.create_window(100, 60, window=label1)
entry1 = Entry(root)
entry1.grid(row=0, column=1)
# canvas1.create_window(300, 60, window=entry1)

# Create Calendar input for Vesting Start Date
label2 = Label(root, text='Vesting Start Date: ').grid(row=1, column=0)
# canvas1.create_window(100, 80, window=label2)
# entry2 = tk.Entry(root)
# canvas1.create_window(300, 80, window=entry2)
sel1=StringVar() # declaring string variable
cal1=DateEntry(root, selectmode='day', textvariable=sel1)
cal1.grid(row=1,column=1,padx=20)
def my_upd1(*args):
    l1.config(text=sel1.get())

l1=Label(root, bg='yellow') # label to display date
l1.grid(row=1, column=2)

sel1.trace('w',my_upd1)

# Create Calendar input for Vesting End Date
sel2=StringVar()
label3 = Label(root, text='Vesting End Date: ').grid(row=2, column=0)
cal2=DateEntry(root, selectmode='day', textvariable=sel2)
cal2.grid(row=2,column=1,padx=20)
def my_upd2(*args):
    l2.config(text=sel2.get())

l2=Label(root, bg='yellow') # label to display date
l2.grid(row=2, column=2)

sel2.trace('w',my_upd2)

# Create Toggle for Cliff period
is_on = True
label4 = Label(root,
    text = "Cliff Period Enabled",
    fg = "green")

label4.grid(row=3, column=0)

def switch():
    global is_on
    # determine is on or off
    if is_on:
        label4.config(text = "Cliff Period DISABLED", fg = "grey")
        is_on = False
    else:
        label4.config(text = "Cliff Period ENABLED", fg = "green")
        is_on = True

cliff_button = Button(root, text = "Toggle", bd=0, command = switch)
cliff_button.grid(row=3, column=1)

# Create function to find time between dates
from dateutil.relativedelta import relativedelta

def months_between(date1, date2):
    difference = relativedelta(date2, date1)
    return (difference.months + 12 * difference.years)


# Create Command for Execute button
def myClick():
    global total_options
    total_options = int(entry1.get())

    global vesting_start
    vesting_start = (cal1.get_date())

    global vesting_end
    vesting_end = (cal2.get_date())
    
    # Display number of months
    output1a = Label(root, text="# of Months: ")
    output1a.grid(row=5, column=0)

    if is_on == False:
        vesting_months = (months_between(vesting_start, vesting_end))
        output1b = Label(root, text=str(vesting_months))
        output1b.grid(row=5, column=1)
    else:
        vesting_months = (int(months_between(vesting_start, vesting_end) - 11))
        output1b = Label(root, text=str(vesting_months))
        output1b.grid(row=5, column=1)

    first_month = int(total_options / 4)

    # Display first month's vested options (25%)
    output2a = Label(root, text="First Month (25% of shares):")
    output2a.grid(row=6, column=0)
    output2b = Label(root, text="{}".format(first_month))
    output2b.grid(row=6, column=1)

    # Display number of options vested each month after
    output3a = Label(root, text="Number of options per month after 1st:")
    output3a.grid(row=7, column=0)


myButton = Button(root, text="Execute", command=myClick).grid(row=4,column=0)

root.mainloop()


# label3 = tk.Label(root, text='Vesting End Date: ')
# canvas1.create_window(100, 60, window=label3)
# entry3 = tk.Entry(root)
# canvas1.create_window(300, 60, window=entry3)