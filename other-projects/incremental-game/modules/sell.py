#!/usr/bin/python3
from .check import check
from .classes import Statistics

def sell(company: Statistics):
    company = check(company)

    return company
