#!/usr/bin/python3
from .classes import Tree

def tree_counter(trees):

    swedish_species = input("Input SWEDISH species name: ").lower()
    latin_species = input("Input LATIN species name: ").lower()

    
    species = {
        "swedish": swedish_species,
        "latin": latin_species
    }

    amount = 0
    for tree in trees:
        if tree.is_species(species) == True:
            amount = amount + 1

    print(amount)

    return amount