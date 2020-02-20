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

#get user input and store it into an array
user_input = input('Enter year and a month (example: 2020 03): ').split(' ')
#use list comprehension to remove any values that aren't numeric and convert them to integers
user_input = [int(i) for i in user_input if i.isnumeric()]

#get current year and month
now = datetime.now()
year = now.year
month = now.month

#check user_input length; update year and month is needed
if len(user_input) > 1:
  year = user_input[0]
  month = user_input[1]
elif len(user_input) == 1:
  year = user_input[0]

#print calendar in terminal
calendar.TextCalendar().prmonth(year, month)