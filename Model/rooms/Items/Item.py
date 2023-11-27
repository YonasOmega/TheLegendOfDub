from abc import ABC, abstractmethod
from Model.Characters.hero.Heroes import Hero


class Item(ABC):
    __itemType = None

    def __init__(self, item: str):
        self.__itemType = item

    def __str__(self):
        return self.__itemType

    @abstractmethod
    def effect(self, hero: Hero):
        pass
