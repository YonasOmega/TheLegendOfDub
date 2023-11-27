import random

from Model.rooms.Items.Item import Item
from Model.Characters.hero.Heroes import Hero
from Model.DungeonGenerator import DungeonGenerator


class Vision_Potion(Item):

    def __init__(self):
        super().__init__("Vision Potion")

    # Get's what is inside surrounding rooms
    def effect(self, Dungeon: DungeonGenerator):
        return Dungeon.__str__()

    # Idea for effect#
    '''
    1. Get the player's current position. (this is the thing we don't have)
    2. Pass that current position to the Dungeon and map(or print) it out. (This is something we don't really have either.)
    3. The surrounds should have some sort of marker indicating what contains them. (Don't have either)
    '''
"""
    def effect(self, Dungeon: DungeonGenerator, Hero: Hero):
        postion_y = Hero.postion()[0] # Don't have this
        postion_x = Hero.postion()[1] # dont have this
        
        # Convert each the surronding areas to a string and return
        # Edge case We're in a postion that all the to the top, bottom, left, right, or corner
        string = ""
        prefix = ""
        for col in range(-1, 1):
            for row in range(-1, 1):
                string = string + prefix + Dungeon.get_maze()[postion_y + col][postion_x + row]
                prefix = " "
            prefix = ""
            string += "\n"
        return string
"""

# potion = Vision_Potion()
# print(potion)
# effect = potion.effect(Dungeon=DungeonGenerator(10, 10))
# print(effect)
