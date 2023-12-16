import random

from Model.rooms.Items.Item import Item
from Model.Characters.hero.Heroes import Hero


class Health_Potion(Item):
    """
    Represents a health potion item in the game.
    Inherits from Item class.
    """
    def __init__(self):
        """
        Initializes a Health Potion instance.
        """
        super().__init__("Health Potion")

    def effect(self, hero: Hero):
        """
        Restores health points to the hero when used.

        Parameters:
            hero (Hero): The hero using the health potion.

        Effect:
            Increases the hero's health by a random amount between 5 and 15.
        """
        health = random.randint(5, 15)
        hero.set_health(health)
