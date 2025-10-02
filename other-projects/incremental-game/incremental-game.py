#!/usr/bin/python3
import datetime as dt

from modules.classes import Machine
from modules.classes import Upgrade
from modules.classes import Statistics
from modules import buy
from modules import check
from modules import click
from modules import sell

available_machines = {
    "basic": Machine("Basic Producer", "\"A basic producer for all your basic producing needs\"", 1, 50),
    "medium": Machine("Medium Producer", "\"A medium level producer for faster production\"", 5, 150),
    "advanced": Machine("Advanced Producer", "\"An advanced production facility for ludicrous speed\"", 20, 400),
}

available_upgrades = {
    "basic": Upgrade("Basic Upgrade", "\"A basic upgrade\"", 0.1, 200, 1)
}

def main():

    company = Statistics(
        money = 10,
        production = 0,
        factor = 1,
        last_check = dt.datetime.now(),
        owned_machines = [],
        owned_upgrades = [])

    # Main game "loop":
    while True:
        cmd = input("What do you wish to do? \n")

        if (cmd == "check"):
            check.check(company)

        elif (cmd == "buy"):
            company = buy.buy(company)

        elif (cmd == "sell"):
            company = sell.sell(company)

        elif (cmd == "click"):
            company = click.click(company)

        elif (cmd == "help"):
            print("Commands:\n" \
            "check - see your stats\n" \
            "buy - buy machines\n" \
            "sell - sell machines\n" \
            "click - generate money (set amount)\n" \
            "help - display this list\n")

        else:
            print("Not valid command, please enter again (enter \"help\" for help)")

main()