import random

from Model.rooms.Items.Item import Item
from Model.Characters.hero.Heroes import Hero
from Model.DungeonGenerator import DungeonGenerator


class Vision_Potion(Item):
    """
    Represents a vision potion item in the game.
    Inherits from Item class.
    """

    def __init__(self):
        """
        Initializes a Vision Potion instance.
        """
        super().__init__("Vision Potion")

    # Get's what is inside surrounding rooms
    def effect(self, Dungeon: DungeonGenerator):
        """
        Reveals the surroundings in the dungeon when used.

        Parameters:
            Dungeon (DungeonGenerator): The current dungeon generator instance.

        Returns:
            str: A string representation of the surroundings in the dungeon.
        """
        return Dungeon.__str__()