#!/usr/bin/python3
import math

def delta_theta(longs, lats):
    # Calculate the angle between two positions
    # Not sure if this is correct spot for this function

    delta_lat = abs(lats[0] - lats[1])

    variable = math.sin(math.radians(longs[0])) * math.sin(math.radians(longs[1])) +\
        math.cos(math.radians(longs[0])) * math.cos(math.radians(longs[1]))\
        * math.cos(math.radians(delta_lat))

    # If variable > 1 this is a rounding error and needs to be corrected:
    if variable > 1.0:
        variable = 1.0

    theta = math.acos(variable)
    
    return theta