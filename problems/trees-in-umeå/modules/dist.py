#!/usr/bin/python3
import math
import random
from sys import float_info

from .classes import Tree

AVAILABLE_COMMANDS = ["point-tree", "tree-tree", "find-closest", "closest-trees"]

def dist(trees: list[Tree]):

    cmd = ""
    while ((cmd.lower() in AVAILABLE_COMMANDS) == False):
        cmd = input("What type of distance do you want to calculate? ")

        if ((cmd.lower() in AVAILABLE_COMMANDS) == False):
            print("Not a valid command. Valid commands: " + 
                  str(AVAILABLE_COMMANDS))
    
    if cmd == "point-tree":
        point = get_point()
        tree = select_tree(trees)

        # Calculate the distance between point and tree
        distance = tree.distance_to_point(point)
        print(distance)

    elif cmd == "tree-tree":
        # Set tree1 as first tree
        print("Select the first tree:")
        tree1 = select_tree(trees)

        # Set tree2_index as second tree
        print("Select the second tree:")
        tree2 = select_tree(trees)

        # Calculate distance between tree1 and tree selected with tree2_index
        distance = tree1.distance_to_point(tree2.coordinates)
        print(distance)

    elif cmd == "find-closest":
        # Set origin_index
        print("Select the tree you want to be the origin of your search:")
        origin = select_tree(trees)

        closest_tree = nearest_tree(origin, trees)
        print("Closest tree is " + 
              str(closest_tree["nearest_tree"].species_swedish) +
              " at " + 
              str(closest_tree["nearest_tree"].coordinates) +
              " with distance " +
              str(closest_tree["closest_distance"]))

def select_tree(trees):
    # Select a tree from trees

    tree_index = "-1"
    while ((is_int(tree_index) == False)
           or
           (((int(tree_index)) in range(len(trees))) == False)):
        
        tree_index = input(
            "Input tree index you want to calculate distance to (MAX: " +
            str(len(trees) - 1) + ") " )

        if (is_int(tree_index) == False):
            print("Not an integer")
        elif (((int(tree_index)) in range(len(trees))) == False):
            print("Index not in range, range is: 0:" + str(len(trees) - 1))

    tree = trees[int(tree_index)]

    return tree


def get_point():

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
    
    return point

def nearest_tree(origin: Tree, trees: list[Tree]):
    # Set closest_distance to insanely large number
    closest_distance = float_info.max
    nearest_tree = Tree("", "", "", "", "", "")

    for tree in trees:
        distance = origin.distance_to_point(tree.coordinates)
        if (tree == origin):
            pass
        elif (distance < closest_distance):
            closest_distance = distance
            nearest_tree = tree

    return {
        "nearest_tree": nearest_tree,
        "closest_distance": closest_distance
    }

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