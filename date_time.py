"""
Date: 08 - 08 - 2022
Author: David Agor
Program: The Date, Time and Datetime Classes
"""
from datetime import date
from datetime import time
from datetime import datetime


def main():
    #Date objects
    today = date.today()
    print("Today's date is",today)

    print("Date components:", today.day, today.month, today.year)

    print("Today's weekday @ is", today.weekday())

    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    print("Which is a:", days[today.weekday()])


    #now working with DATETIME OBJECTS
    today1 = datetime.now()
    print("The current date and time is", today1)

    t = datetime.time(datetime.now())
    print(t)

print(main())
