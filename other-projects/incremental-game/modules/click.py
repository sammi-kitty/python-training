#!/usr/bin/python3
from .classes import Statistics
import datetime as dt

def click(company: Statistics):
    generated_money = 10
    company.money = company.money + generated_money

    print("You click and generate " + str(generated_money) + ".")
    print("This means that your new balance is " + str(company.money))

    return company