#!/usr/bin/python3
import os

# A bunch of global variables used in the project

def PROJECT_DIRECTORY(): 
    return os.path.join(os.path.dirname(__file__))

def FORMATTED_FILE(): 
    return os.path.join(PROJECT_DIRECTORY(), "data", "formatted_csv.csv")

def EARTH_RADIUS():
    return 6371000.0