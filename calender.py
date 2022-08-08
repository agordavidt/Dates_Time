"""
Program: Generate the birth calendar of users
Date: 08 -08 2022
Author: Agor David
"""
import calendar

def birth_calendar():
    birth_year = int(input("What's your year of birth: "))
    birth_month = int(input("What is your birth month: "))

    print(calendar.month(birth_year, birth_month))

birth_calendar()