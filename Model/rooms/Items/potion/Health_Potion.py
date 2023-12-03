import random
from Model.rooms.Items.Item import Item
from Model.Characters.hero.Heroes import Hero

class Health_Potion(Item):
    """
    Represents a health potion in the game.

    This class inherits from the Item class and is specifically used for health potions.
    Health potions have an effect that increases the health of a Hero character.

    Attributes inherited from Item:
        __name (str): Name of the item.
    """

    def __init__(self):
        """
        Initializes a Health Potion item.
        """
        super().__init__("Health Potion")

    def effect(self, hero: Hero):
        """
        Apply the health potion's effect to a Hero.

        This method increases the Hero's health by a random amount between 5 and 15.

        :param hero: The Hero object that will receive the health increase.
        :return: The new health value of the Hero after applying the potion.
        """
        return hero.set_health(random.randint(5, 15))

# hp = Health_Potion()
# print(hp)

# priest = Priestess("Bob")
# print(priest)
#
# priest.receive_damage(20)
# print(priest)
#
# hp.effect(priest)
# print(priest)

