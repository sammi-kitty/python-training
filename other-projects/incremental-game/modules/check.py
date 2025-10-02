#!/usr/bin/python3
from .classes import Statistics
import datetime as dt

def check(company: Statistics):
    time_delta = dt.datetime.now() - company.last_check

    generated_money = company.production * company.factor * time_delta.total_seconds()
    company.money = company.money + generated_money

    print("Since the last check, you have generated " + str(generated_money) + ".\n")
    print("This means that your company balance is now " + str(company.money) + ".\n")

    print("The company owns the following machines:\n")
    for machine in company.owned_machines:
        print(str(machine.name) + ", producing " + str(machine.production) + "/s\n")

    print("And the following upgrades:")
    for upgrade in company.owned_upgrades:
        print(str(upgrade) + "\n")

    return