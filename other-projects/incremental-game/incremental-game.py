#!/usr/bin/python3
import datetime as dt

from modules.classes import Statistics
from modules import buy, check, click, sell

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