class Pillar:
    """
    Represents a pillar in the dungeon game.

    This class encapsulates the concept of a pillar, which can be one of the foundational concepts in the game
    (like Abstraction, Encapsulation, Inheritance, Polymorphism).

    Attributes:
        __pillar (str): A string representing the type of the pillar.
    """

    def __init__(self, pillar: str):
        """
        Initialize a Pillar instance with a specified type.

        :param pillar: A string representing the type of the pillar.
        """
        self.__pillar = pillar

    @property
    def pillar(self):
        """
        Get the type of the pillar.

        :return: The type of the pillar as a string.
        """
        return self.__pillar

    @pillar.setter
    def pillar(self, value):
        """
        Set the type of the pillar.

        :param value: A string representing the new type of the pillar.
        """
        self.__pillar = value

    def __str__(self):
        """
        Return a string representation of the Pillar object.

        :return: The type of the pillar as a string.
        """
        return f"{self.__pillar}"
