#!/usr/bin/python3
import math
import random

from .classes import Tree

def dist(trees: list[Tree]):

    print(range(len(trees)))

    # Enter longitude
    longitude = ""
    while (is_float(longitude) == False):
        longitude = input("Enter longitude for the point you want to calculate")

        if (is_float(longitude) == False):
            print("Not a float.")

    # Enter latitude
    latitude = ""
    while (is_float(latitude) == False):
        latitude = input("Enter latitude for the point you want to calculate")

        if (is_float(latitude) == False):
            print("Not a float.")

    point = {
        "long": float(longitude),
        "lat": float(latitude)
    }

    # Select the tree you want to compare distance to
    tree_index = "-1"
    while ((is_int(tree_index) == False)
           or
           (((int(tree_index)) in range(len(trees))) == False)):
        tree_index = input("Input tree index you want to calculate distance to (MAX: " + str(len(trees) - 1) + ") " )

        if (is_int(tree_index) == False):
            print("Not an integer")
        elif (((int(tree_index)) in range(len(trees))) == False):
            print("Index not in range, range is: 0:" + str(len(trees) - 1))
    
    # Evaluate the distance between Tree.coordinates and point
    distance = trees[int(tree_index)].distance_to_point(point)
    print(distance)

def is_float(value):
    # Check if a value is a float
    try:
        float(value)
        return True
    
    except:
        return False
    
def is_int(value):
    # Check if a value is an int
    try:
        int(value)
        return True
    
    except:
        return False