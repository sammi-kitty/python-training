#!/usr/bin/python3
import csv
import os

from .classes import Tree
from global_variables import PROJECT_DIRECTORY, FORMATTED_FILE

def tree_organiser():

    file_path = ""
    while (is_valid_filename(file_path) == False):
        filename = input("Insert filename containing tree data (WITHOUT relative path): ")

        file_path = os.path.join(PROJECT_DIRECTORY, "data", filename)
        print(file_path)

        if (is_valid_filename(file_path) == False):
            print("Not a valid file name.")

    # Take the file of trees and make it CSV compliant by swapping out ; for ,
    # The new file is FORMATTED_FILE
    csv_compliance(file_path)

    trees = []
    with open(FORMATTED_FILE) as file:
        header = next(file)
        reader = csv.reader(file)

        for row in reader:
            trees.append(tree_converter(row))

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
        float(str(row[1]).strip())
        ]
    tree.tree_type = str(row[2]).lower()
    tree.species_latin = str(row[3]).lower()
    tree.species_swedish = str(row[4]).lower()
    tree.plantation_type = str(row[5]).lower()
    tree.date = row[6] #PLACEHOLDER USE PROPER DATETIME INSTEAD
    
    return tree

def is_valid_filename(input):
    try:
        with open(input) as file:
            pass
        return True
    except:
        return False