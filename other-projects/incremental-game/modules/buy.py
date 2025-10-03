#!/usr/bin/python3
from .classes import Statistics, Machine, Upgrade

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
    
    answer = ""
    while (contains(["machines", "upgrades"], answer) == False):
        answer = input("What do you want to buy? \n")

        if contains(["machines", "upgrades"], cmd):
            print("You are now buying: " + answer)
        else:
            print("That is not a valid type of thing to buy. The valid types are: machines, upgrades")

    if (type_to_buy == "machines"):
        stock = AVAILABLE_MACHINES.copy()
    else:
        stock = AVAILABLE_UPGRADES.copy()
    
    print("You are now buying: " + str(type_to_buy.capitalize()))
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
            machine_to_buy = element

    amount_to_buy = ""
    while (is_integer(amount_to_buy) == False 
           or 
           affords(amount_to_buy, machine_to_buy, company.money) == False):
        amount_to_buy = input("What amount of the selected stock do you wish to purchase?\n")

        if (is_integer(amount_to_buy) and affords(amount_to_buy, machine_to_buy, company.money)):
            print("Now purchasing: " + str(amount_to_buy) + "x " + str(machine_to_buy))

        if (is_integer(amount_to_buy) == False):
            print("Not an integer.")
        if (affords(amount_to_buy, machine_to_buy, company.money) == False):
            print("You do not afford that purchase. To exit this purchase, enter \"exit\"")
        
        if (amount_to_buy == "exit"):
            return company

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

def affords(amount, price, money):
    if (amount * price <= money):
        return True
    else:
        return False