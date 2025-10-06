#!/usr/bin/python3
from .classes import Tree
import csv

FORMATTED_FILE = "/home/samantha/Code/python-training/problems/trees-in-umeå/formatted_csv.csv"

def tree_organiser(filename):

    # Take the file of trees and make it CSV compliant by swapping out ; for ,
    # The new file is FORMATTED_FILE
    csv_compliance(filename)

    trees = []
    with open(FORMATTED_FILE) as file:
        heading = next(file)
        reader = csv.reader(file)

        for row in reader:
            trees.append(tree_converter(row))
    
    print(trees)

    return trees

def csv_compliance(filename):
    # Swap all ; for , and save the result in FORMATTED_FILE

    table = str.maketrans(";", ",")

    file_rows = []
    with open(filename) as file:
        for row in file:
            file_rows.append(row.translate(table))

    with open(FORMATTED_FILE, "w") as file:
        file.writelines(file_rows)

    return

def tree_converter(row):
    tree = Tree([],"","","","","")

    tree.coordinates = [
        float(row[0]), 
        float(row[1][1:len(row[1])])
        ]
    
    return tree