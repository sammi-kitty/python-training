#!/usr/bin/python3

class Tree:
    def __init__(self, coordinates, tree_type, species_latin, species_swedish, plantation_type, date):
        self.coordinates = coordinates
        self.tree_type = tree_type
        self.species_latin = species_latin
        self.species_swedish = species_swedish
        self.plantation_type = plantation_type
        self.date = date

    def __str__(self):
        return (self.coordinates, 
                self.tree_type, 
                self.species_latin, 
                self.species_swedish, 
                self.plantation_type, 
                self.date)