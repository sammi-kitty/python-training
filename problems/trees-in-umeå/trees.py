#!/usr/bin/python3
import os

from modules.classes import Tree
from modules.tree_organiser import tree_organiser
from modules.tree_counter import tree_counter

VALID_COMMANDS = ["load trees", "help"]

def main():
    
    while True:
        cmd = input("Insert cmd: ")

        if (cmd == "load trees"):
            print("organising trees")
            trees = tree_organiser()

        elif (cmd == "count"):
            print("counting trees")
            tree_counter(trees)


        elif (cmd == "help"):
            print("Available commands: \n" + str(VALID_COMMANDS))

        else:
            print("That is not a valid command")

main()