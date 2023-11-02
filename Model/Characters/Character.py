from abc import ABC, abstractmethod


class PlayableCharacter(ABC):

    __my_type = None
    __my_health = None
    __my_strength = None
    __my_speed = None
    __my_Items = None

    def __init__(self, the_character: str, the_health: int, the_strength: int, the_speed: int, the_items: list):
        self.__my_type = the_character
        self.__my_health = the_health
        self.__my_strength = the_strength
        self.__my_speed = the_speed
        self.__my_Items = the_items

    @abstractmethod
    def health(self):
        pass

    @abstractmethod
    def strength(self):
        pass

    @abstractmethod
    def speed(self):
        pass

    @abstractmethod
    def pull_items(self):
        pass

    def __str__(self):
        return f"{self.__my_type}\n" \
               f"health: {self.__my_health}\n" \
               f"strength: {self.__my_strength}\n" \
               f"Speed: {self.__my_speed}\n" \
               f"Items: {self.__my_Items}\n"





