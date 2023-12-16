from abc import ABC, abstractmethod
from Model.Characters.hero.Heroes import Hero


class Item(ABC):
    """
    Abstract base class for items in the game.

    Attributes:
        __itemType (str): The type or name of the item.
    """
    __itemType = None

    def __init__(self, item: str):
        """
        Initializes an Item instance.

        Parameters:
            item (str): The type or name of the item.
        """
        self.__itemType = item

    def __str__(self):
        """
        String representation of the Item.

        Returns:
            str: The type or name of the item.
        """
        return self.__itemType

    @abstractmethod
    def effect(self, hero: Hero):
        """
        Abstract method to define the effect of the item when used.

        Parameters:
            hero (Hero): The hero using the item.
        """
        pass
