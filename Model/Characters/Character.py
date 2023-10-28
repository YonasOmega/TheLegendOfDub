from abc import ABC, abstractmethod


class Character(ABC):
    __myType = 0

    def __init__(self, type):
        self.__myType = type

    @abstractmethod
    def __str__(self):
        pass


