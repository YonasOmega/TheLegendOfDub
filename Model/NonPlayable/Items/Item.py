from abc import ABC, abstractmethod


class Item(ABC):
    __itemType = 0

    def __init__(self, item):
        self.__itemType = item

    def __str__(self):
        pass
