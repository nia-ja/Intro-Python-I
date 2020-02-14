"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

current = datetime.now()
cal = calendar.TextCalendar()
arg = sys.argv

def toNum(arg):
    if arg.isdigit():
        return int(arg)
    else:
        return False


if (len(arg) == False):
    print('Expecting input in the form of month [year]')
    exit()

month = len(arg) > 1 and toNum(arg[1]) or current.month
year = len(arg) > 2 and toNum(arg[2]) or current.year

cal.prmonth(year, month)