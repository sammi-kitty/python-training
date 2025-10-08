#!/usr/bin/python3
import math

def delta_theta(longs, lats):
    # Calculate the angle between two positions
    # Not sure if this is correct spot for this function

    delta_lat = abs(lats[0] - lats[1])

    theta = math.acos(
        (math.sin(math.radians(longs[0])) * math.sin(math.radians(longs[1]))
        +
        math.cos(math.radians(longs[0])) * math.cos(math.radians(longs[1])))
        * math.cos(math.radians(delta_lat)))
    
    return theta