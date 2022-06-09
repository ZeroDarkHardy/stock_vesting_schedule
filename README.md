# stock_vesting_schedule
Creating a GUI for performing simple equity cap-table calculations using Python w/ TKinter.

## Overview of Project
My client works in the legal department at a tech company.  Part of her job involves overseeing her company's equity cap table, and assisting when a shareholder decides to excercize their stock options.  Unfortunately, there are bugs in the equity management software her company uses, which sometimes create small inconsitencies in their stock vesting schedules.  <br/>The client had been verifying the vesting schedules using an Excel spreadsheet, and my aim was to expedite that process by creating a user-friendly GUI that would perform the necessary calculations to verify the vesting schedule totals.  Verification of this kind is only necessary when a shareholder intends to excercize their options before the full sum have reached their vesting period.<br/>
<br/>

## Resources
Software/Languages: Python 3.7.11, TKinter, TKcalendar, Pyinstaller, Visual Studio Code 1.68.0

## Project Constraints
According to my client, all stock options granted by her company are on a 48 month vesting schedule.  While
that means that all options vest at a rate of 2.08333% per month, many option grants contain a "cliff period" during which no shares officially vest (this period is 11 full calendar months).  On the first day of the 12th month, the cliff period expires and a lump amount of options (25% of grant total) become immediately vested.  Each month after that, the options vest at a rate of 1/48 of total per month, calculated to 5 decimal places.<br/>
<br/>
Though the rate of vesting is monitored out to 5 decimal places, when a total is generated (at time of excercizing), this total is rounded ***down*** to the nearest integer.<br/>
<br/>
The client wants the following features to be present in the GUI:
-   A text entry field for the total number of options in the grant.
-   Two calendar drop-down style menus to accept date inputs for the start and end of vesting period (meaning the date of the original grant and the date of excercize).
-   A clickable toggle to enable/disable the "cliff period" in the vesting cycle.