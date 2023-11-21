from Model.Characters.Character import Character


class Goblin(Character):
    __type = "Goblin"
    __health = 10
    __strength = 2
    __speed = 4
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


