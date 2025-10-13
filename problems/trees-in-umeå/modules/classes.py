#!/usr/bin/python3
from global_variables import EARTH_RADIUS
from .dist_math import delta_theta

class Tree:
    def __init__(self, coordinates, tree_type, species_latin, species_swedish, plantation_type, date):
        self.coordinates = coordinates
        self.tree_type = tree_type
        self.species_latin = species_latin
        self.species_swedish = species_swedish
        self.plantation_type = plantation_type
        self.date = date

    def __str__(self):
        return (str(self.coordinates) + " " +
                str(self.tree_type) + " " +
                str(self.species_latin) + " " +
                str(self.species_swedish) + " " +
                str(self.plantation_type) + " " +
                str(self.date))

    def is_species(self, species):
        # Check if tree belongs to certain species

        if (
            (str(self.species_swedish).find(species["swedish"]) != -1)
            and
            (str(self.species_latin).find(species["latin"]) != -1)
            ):
            return True
        else:
            return False
        
    def distance_to_point(self, point):
        # Calculate the distance from self.coordinates to point

        theta = delta_theta(
            [self.coordinates["long"], point["long"]],
            [self.coordinates["lat"], point["lat"]])

        distance = EARTH_RADIUS() * theta

        return distance