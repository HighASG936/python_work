"""" """
from random import randint

class Dice:
    """ """
    def __init__(self):
        """ """
        self.sides = 1
    
    def roll_dice(self, sides):
        self.sides = sides
        print(randint(1, self.sides))
        
        