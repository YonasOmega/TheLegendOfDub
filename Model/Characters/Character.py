from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def __str__(self):
        pass


