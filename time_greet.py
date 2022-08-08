"""
Program: To greet users based on time of the day
Date: 08 - 08 - 2022
Author: Agor David
"""

import datetime

def greet():
    user = input("Enter your Name: ")
    now = datetime.datetime.now()
    hour = now.hour

    if hour < 12:
        greeting = "Good morning "+ user
    elif hour < 18:
        greeting = "Good afternoon "+ user
    else:
        greeting = "Good night "+ user

    print("Hello! {}".format(greeting))

greet()