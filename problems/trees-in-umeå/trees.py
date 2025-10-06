#!/usr/bin/python3
import datetime as dt
import csv

from modules.classes import Tree

def main():
    
    # answer = ""
    # while (is_valid_file(answer) == False):
    #     answer = input("Insert filename containing tree data: ")

    #     if (is_valid_file(answer) == False):
    #         print("Not a valid file name.")
    
    file = []
    with open(".trad_dobelns_park.csv") as opened_file:
        print(opened_file)

def is_valid_file(input):
    print(input)
    try:
        with open(input) as file:
            print(file)
            pass
        return True
    except:
        return False
    
main()