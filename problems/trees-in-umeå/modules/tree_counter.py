#!/usr/bin/python3
from .classes import Tree

def tree_counter(trees):

    # Species name
    swedish_species = input("Input SWEDISH species name: ").lower()
    latin_species = input("Input LATIN species name: ").lower()

    # overcount = ""
    # while (overcount in ["True", "False"]) == False:
    #     overcount = input("Overcount? (True/False) ")

    #     if (overcount in ["True", "False"]) == False:
    #         print("Not a valid answer.")
        
    # overcount = bool(overcount)
    species = {
        "swedish": swedish_species,
        "latin": latin_species
    }

    # Count amount of trees with certain species
    amount = 0
    for tree in trees:
        if tree.is_species(species) == True:
            amount = amount + 1

    # if overcount:
    #     for tree in trees:
    #         if tree.is_species({
    #             "swedish": "",
    #             "latin": ""
    #         }):
    #             amount = amount + 1

    print(amount)