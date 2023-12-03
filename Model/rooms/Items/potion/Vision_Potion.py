import random
from Model.rooms.Items.Item import Item
from Model.DungeonGenerator import DungeonGenerator

class Vision_Potion(Item):
    """
    Represents a vision potion in the game.

    This class inherits from the Item class and is specifically used for vision potions.
    Vision potions have a unique effect that reveals the layout or contents of the surrounding rooms in the dungeon.

    Attributes inherited from Item:
        __itemType (str): Name of the item.
    """

    def __init__(self):
        """
        Initializes a Vision Potion item.
        """
        super().__init__("Vision Potion")

    def effect(self, dungeon: DungeonGenerator):
        """
        Apply the vision potion's effect on the given dungeon.

        This method returns a string representation of the dungeon, typically revealing its layout
        or the contents of the surrounding rooms.

        :param dungeon: An instance of DungeonGenerator representing the dungeon to be revealed.
        :return: A string representation of the dungeon layout or contents.
        """
        return dungeon.__str__()


    # Idea for effect#

    # 1. Get the player's current position. (this is the thing we don't have)
    # 2. Pass that current position to the Dungeon and map(or print) it out. (This is something we don't really have either.)
    # 3. The surrounds should have some sort of marker indicating what contains them. (Don't have either)
    #
    #
    # def effect(self, Dungeon: DungeonGenerator, Hero: Hero):
    #     postion_y = Hero.postion()[0] # Don't have this
    #     postion_x = Hero.postion()[1] # dont have this
    #
    #     # Convert each the surronding areas to a string and return
    #     # Edge case We're in a postion that all the to the top, bottom, left, right, or corner
    #     string = ""
    #     prefix = ""
    #     for col in range(-1, 1):
    #         for row in range(-1, 1):
    #             string = string + prefix + Dungeon.get_maze()[postion_y + col][postion_x + row]
    #             prefix = " "
    #         prefix = ""
    #         string += "\n"
    #     return string


# potion = Vision_Potion()
# print(potion)
# effect = potion.effect(Dungeon=DungeonGenerator(10, 10))
# print(effect)
