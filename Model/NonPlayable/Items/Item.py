from abc import ABC, abstractmethod


class Item(ABC):
    __itemType = None

    def __init__(self, item):
        self.__itemType = item

    @abstractmethod
    def __str__(self):
        pass
