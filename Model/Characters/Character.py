from abc import ABC, abstractmethod


class Character(ABC):
    __myType = ""

    def __init__(self, type: str):
        self.__myType = type

    @abstractmethod
    def __str__(self):
        pass


