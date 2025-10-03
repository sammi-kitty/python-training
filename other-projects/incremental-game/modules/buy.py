#!/usr/bin/python3
from .classes import Statistics, Machine, Upgrade
from .check import check

AVAILABLE_MACHINES = {
    "basic": Machine("Basic Producer", "\"A basic producer for all your basic producing needs\"", 1, 50),
    "medium": Machine("Medium Producer", "\"A medium level producer for faster production\"", 5, 150),
    "advanced": Machine("Advanced Producer", "\"An advanced production facility for ludicrous speed\"", 20, 400),
}

AVAILABLE_UPGRADES = {
    "basic": Upgrade("Basic Upgrade", "\"A basic upgrade\"", 0.1, 200, 1),
    "awesome": Upgrade("Really fucking awesome uppgrade", "\"Fucks the awesome\"", 3, 1000, 1)
}

def buy(company: Statistics):
    company = check(company)

    answer = ""
    while ((answer in ["machines", "upgrades"]) == False):
        answer = input("What do you want to buy? \n")

        if (answer in ["machines", "upgrades"]):
            print("You are now buying: " + answer)
        else:
            print("That is not a valid type of thing to buy. The valid types are: machines, upgrades")

    if (answer == "machines"):
        stock = AVAILABLE_MACHINES.copy()
    else:
        stock = AVAILABLE_UPGRADES.copy()
    
    print("You are now buying: " + answer.capitalize())
    print("Available products:")
    for element in stock.values():
        print(
            str(element.name) 
            + ". Description: " 
            + str(element.description) 
            + ". Price: " 
            + str(element.price))
    
    answer = ""
    while (contains(stock, answer) == False):
        answer = input("What stock do you wish to purchase?\n")

        if contains(stock, answer):
            print("You are now buying: " + str(answer))
        else:
            print("Not a valid stock.")

    for element in stock.values():
        if (element.name.lower() == answer.lower()):
            item_to_buy = element

    print("money" + str(company.money))
    print("item_to_buy" + str(item_to_buy))

    amount_to_buy = ""
    while (is_integer(amount_to_buy) == False 
           or 
           affords(amount_to_buy, item_to_buy, company.money) == False):
        amount_to_buy = input("What amount of the selected stock do you wish to purchase?\n")

        if (is_integer(amount_to_buy) and affords(amount_to_buy, item_to_buy, company.money)):
            print("Now purchasing: " + str(amount_to_buy) + "x " + str(item_to_buy))

        if (amount_to_buy == "exit"):
            return company

        if (is_integer(amount_to_buy) == False):
            print("Not an integer.")
        if (affords(amount_to_buy, item_to_buy, company.money) == False):
            print("You do not afford that purchase. To exit this purchase, enter \"exit\".")

    company.production = company.production + item_to_buy.production * amount_to_buy
    company.money = company.money - item_to_buy.price * amount_to_buy

    return company

def is_integer(value):
    try:
        int(value)
        return True
    
    except:
        return False
    
def contains(set: dict[str, Machine] | dict[str, Upgrade], thing):
    for element in set.values():
        if (thing.lower() == element.name.lower()):
            return True
    return False

def affords(amount, item_to_buy: Machine, money):
    try:
        if ((amount * item_to_buy.price) < money):
            return True
        else:
            return False
    except:
        return False