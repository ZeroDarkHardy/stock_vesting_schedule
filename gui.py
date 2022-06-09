#!/usr/bin/env python

from tkinter import *
import tkinter.font
from tkcalendar import DateEntry
import math

# Create GUI
root = Tk()
# Add Title
root.title("Amanda's Stock Vesting Calculator")
# Add Geometry
root.geometry("800x300")

# create font for larger display widgets
helv25 = tkinter.font.Font( family = "Helvetica", size = 25, weight = "bold")

# Create Total Options Granted field
label1 = Label(root, text='Total Options Granted: ').grid(row=0, column=0)
entry1 = Entry(root)
entry1.grid(row=0, column=1)


# Create Calendar input for Vesting Start Date
label2 = Label(root, text='Vesting Start Date: ').grid(row=1, column=0)
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
label4.config(font=helv25)

def switch():
    global is_on
    # determine is on or off
    if is_on:
        label4.config(text = "Cliff Period DISABLED", fg = "grey")
        is_on = False
        output1b.config(text="               ")
        output2b.config(text="               ")
        output3b.config(text="               ")
        output4b.config(text="               ")
        label4.config(font=helv25)
    else:
        label4.config(text = "Cliff Period ENABLED", fg = "green")
        is_on = True
        output1b.config(text="               ")
        output2b.config(text="               ")
        output3b.config(text="               ")
        output4b.config(text="               ")
        label4.config(font=helv25)

cliff_button = Button(root, text = "Toggle", command = switch)
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
    output1a = Label(root, text="# of Vesting Months: ")
    output1a.grid(row=5, column=0)
    monthly_options = float(total_options / 48)
    
    global output1b
    global output2b

    if is_on == False:
        vesting_months = (months_between(vesting_start, vesting_end))
        ending_total = math.floor(monthly_options * vesting_months)
        output2a = Label(root, text="First Month (25% of shares):")
        output2a.grid(row=6, column=0)
        output2b = Label(root, text="No lump vesting.")
        output2b.grid(row=6, column=1)
    else:
        vesting_months = (int(months_between(vesting_start, vesting_end) - 11))
        
        # Display first month's vested options (25%) if there's a cliff period
        first_month = float(total_options / 4)
        output2a = Label(root, text="First Month (25% of shares):")
        output2a.grid(row=6, column=0)
        output2b = Label(root, text="{}".format(first_month))
        output2b.grid(row=6, column=1)
        ending_total = math.floor(first_month + (float(monthly_options) * (float(vesting_months) - 1)))

    output1b = Label(root, text=str(vesting_months))
    output1b.grid(row=5, column=1)
    # Display number of options vested each month after

    global output3b
        
    output3a = Label(root, text="Number of options per month after 1st:")
    output3a.grid(row=7, column=0)
    output3b = Label(root, text=str("%.5f" % float(monthly_options)))
    output3b.grid(row=7, column=1)
    
    # Display confirmation of total number of options

    global output4b

    output4a = Label(root, text="Total at \n End of Vesting:")
    output4a.grid(row=8, column=0)
    output4b = Label(root, text=str(ending_total))
    output4b.grid(row=8, column=1)

Label(root, text="THESE CALCULATIONS ASSUME A 48 MONTH VESTING SCHEDULE").grid(row=15, column=0)

def clear():
    output1b.config(text="               ")
    output2b.config(text="               ")
    output3b.config(text="               ")
    output4b.config(text="               ")
    

myButton = Button(root, text="Execute", command=myClick).grid(row=4,column=0)

clear_button = Button(root, text="Clear Results", command=clear).grid(row=16, column=0)

root.mainloop()