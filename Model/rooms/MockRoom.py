import random

from Model.rooms.Items.potion.Health_Potion import Health_Potion

class MockRoom():

    def __init__(self):
        self.__healing_potion = None
        self.__pit = None
        self.__entrance = None
        self.__exit = None
        self.__doors = list()

    #Potion#
    def make_potion(self):
        self.__healing_potion = Health_Potion

    def get_potion(self):
        return self.__healing_potion

    def potion(self):
        if random.randint(0,100) < 10:
            self.make_potion()

    #Pit#
    def make_pit(self):
        self.__pit = random.randint(1, 20)

    def get_pit(self):
        return self.__pit

    def pit(self):
        if random.randint(0,100) < 10:
            self.make_pit()

    #entrance and exit #
    def make_entrance(self, position: tuple):
        self.__entrance = position

    def get_entrance(self):
        return self.__entrance

    def make_exit(self, position: tuple):
        self.__exit = position

    def get_exit(self):
        return self.__exit

###--String builders--##
    def north(self):
        north = ""
        if self.__doors.__contains__('n'):
            north = "*-*"
        else:
            north = "***"
        return north

    def south(self):
        south = ""
        if self.__doors.__contains__('s'):
            south = "*-*"
        else:
            south = "***"
        return south

    def center(self):
        center = ""

        if self.__doors.__contains__('w'):
            center = "|"
        else:
            center = "*"

        center = center + " "

        if self.__doors.__contains__('e'):
            center = center + "|"
        else:
            center = center + "*"
        return center

    def __str__(self):
        String = self.north() + "\n"
        String = String + self.center() + "\n"
        String = String + self.south() + "\n"
        return String

