
from Model.Characters.Character import PlayableCharacter


class Warrior(PlayableCharacter):
    __type = "warrior"
    __health = 3
    __strength = 3
    __speed = 3
    __items = list()

    def __init__(self):
        super().__init__(self.__type, self.__health, self.__strength, self.__speed, self.__items)

    def health(self):
        print("health")

    def strength(self):
        print("attack")

    def speed(self):
        print("move")

    def pull_items(self):
        print("item")


