""""Birthday Day Finder"
Objective: Write a Python program that calculates what day of the week your next birthday falls on.
Steps:
Import the datetime library.
Ask the user to input their birthdate in the format YYYY-MM-DD.
Parse the input into a datetime object.
Get the current year and create a datetime object for the next birthday using the month and day from the user's input.
If the birthday for the current year has already passed, calculate it for the next year.
Determine the day of the week for the next birthday using .strftime("%A").
Display the result to the user."""

import datetime
user_input = input("Enter your birth date in format YYYY-MM-DD: ")
# user_input = "1995-05-15"
date_of_birth = datetime.datetime.strptime(user_input, "%Y-%m-%d")
month_of_birth = date_of_birth.month
day_of_birth = date_of_birth.day
current_year = datetime.datetime.now().year
next_birthday = datetime.datetime(current_year, month_of_birth, day_of_birth)
if datetime.datetime.now() > next_birthday:
    next_birthday = datetime.datetime(current_year + 1, month_of_birth, day_of_birth)
print(next_birthday.strftime("%A"))
