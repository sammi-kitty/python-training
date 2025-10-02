#!/usr/bin/python3
from time import sleep
from dataclasses import dataclass

@dataclass
class Machine:
    name: str
    description: str
    production: float
    price: float

@dataclass
class Upgrade:
    name: str
    description: str
    factor: float
    price: float

@dataclass
class Statistics:
    money: float
    production: float
    factor: float
    owned_machines: list[Machine]
    owned_upgrades: list[Upgrade]

available_machines = {
    "basic": Machine("Basic Producer", "\"A basic producer for all your basic producing needs\"", 1, 50),
    "medium": Machine("Medium Producer", "\"A medium level producer for faster production\"", 5, 150),
    "advanced": Machine("Advanced Producer", "\"An advanced production facility for ludicrous speed\"", 20, 400),
}

available_upgrades = {
    "basic": Upgrade("Basic Upgrade", "\"A basic upgrade\"", 1.1, 200)
}

def main():

    company = Statistics(
        money = 10,
        production = 0,
        factor = 1,
        owned_machines = [available_machines["basic"]],
        owned_upgrades = [available_upgrades["basic"]])

    # Main game "loop":
    while True:
        cmd = input("What do you wish to do? \n")

        if (cmd == "check"):
            check(money, factor, owned_machines)

        elif (cmd == "buy"):
            response = buy(money, factor, owned_machines)

            money = response.money
            factor = response.factor
            owned_machines = response.owned_machines

        elif (cmd == "sell"):
            response = sell(money, factor, owned_machines)

            money = response.money
            factor = response.factor
            owned_machines = response.owned_machines

        elif (cmd == "click"):
            money = click(money)

        elif (cmd == "help"):
            print("Commands:\n" \
            "check - see your stats\n" \
            "buy - buy machines\n" \
            "sell - sell machines\n" \
            "click - generate money (set amount)\n" \
            "help - display this list\n")

        else:
            print("Not valid command, please enter again")

def check(company: Statistics):
    print(money)

def buy(company: Statistics):
    print("These are the machines you own:\n")
    print(owned_machines)

def sell(company: Statistics):
    print("These are the machines you own:\n")
    print(owned_machines)

def click(company: Statistics):
    return (money + 10)

main()