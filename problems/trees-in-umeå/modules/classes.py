#!/usr/bin/python3
import math

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
        if (
            (str(self.species_swedish).find(species["swedish"]) != -1)
            and
            (str(self.species_latin).find(species["latin"]) != -1)
            ):
            return True
        else:
            return False
        
    def dist(self, coord):
        delta_x = self.coordinates[0] - coord[0]
        delta_y = self.coordinates[1] - coord[1]
        return math.sqrt(math.pow(delta_x) + math.pow(delta_y))