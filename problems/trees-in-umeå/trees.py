#!/usr/bin/python3
import datetime as dt
import csv

from modules.classes import Tree
from modules.tree_organiser import tree_organiser

def main():
    
    answer = ""
    while (is_valid_file(answer) == False):
        answer = input("Insert filename containing tree data: ")

        if (is_valid_file(answer) == False):
            print("Not a valid file name.")

    trees = tree_organiser(answer)

def is_valid_file(input):
    try:
        with open(input) as file:
            pass
        return True
    except:
        return False

main()