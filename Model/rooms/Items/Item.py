from abc import ABC, abstractmethod
from Model.Characters.hero.Heroes import Hero

class Item(ABC):
    """
    Abstract base class representing a general item in the game.

    This class serves as a template for various types of items that can be encountered or used in the game.
    Each item has a specific type and an effect when used, especially on Hero characters.

    Attributes:
        __itemType (str): The type of the item, described as a string.
    """

    def __init__(self, item: str):
        """
        Initializes an Item with a specified type.

        :param item: A string representing the type of the item.
        """
        self.__itemType = item

    def __str__(self):
        """
        Return a string representation of the Item.

        :return: The type of the item as a string.
        """
        return self.__itemType

    @abstractmethod
    def effect(self, hero: Hero):
        """
        Abstract method to define the effect of the item on a Hero.

        This method should be implemented by subclasses to specify how the item affects a Hero character.

        :param hero: The Hero object on which the item's effect will be applied.
        """
        pass
