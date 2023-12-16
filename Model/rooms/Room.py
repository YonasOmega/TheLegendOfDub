import random
import sqlite3

from Model.rooms.Items.potion.Health_Potion import Health_Potion
from Model.rooms.Items.potion.Vision_Potion import Vision_Potion
# from Model.Characters.Monsters.Ogre import Ogre
# from Model.Characters.Monsters.Skeleton import Skeleton
# from Model.Characters.Monsters.Gremlin import Gremlin
from Model.Characters.Monsters.Monster import Ogre
from Model.Characters.Monsters.Monster import Skeleton
from Model.Characters.Monsters.Monster import Gremlin
from Model.rooms.Items.Pillar.OOP import Polymorphism
from Model.rooms.Items.Pillar.OOP import Encapsulation
from Model.rooms.Items.Pillar.OOP import Inheritance
from Model.rooms.Items.Pillar.OOP import Abstraction


class Room:

    def __init__(self, location: tuple):
        self.__potion = None
        self.__pit = None
        self.__entrance = None
        self.__exit = None
        self.__doors = list()
        self.__monster = None
        self.__pillar = None
        self.__location = location

    def generate(self, special: str):
        self.generate_special(special)

    def generate_non_special(self):
        self.generate_potion()
        self.generate_pit()
        self.generate_monster()

    def generate_pillar(self, special: str):
        if special == "E":
            self.make_encapsulation()
        elif special == "P":
            self.make_polymorphism()
        elif special == "I":
            self.make_inheritance()
        elif special == "A":
            self.make_abstraction()

        # Ogre would have been made.
        self.__monster.position = self.__location

    def generate_special(self, special: str):
        if special == "X":
            self.make_entrance()
        elif special == "Y":
            self.make_exit()
        elif special == "1":
            self.generate_non_special()
        elif special != "0":
            self.generate_pillar(special)

    # -------- Pillar ---------#
    @property
    def pillar(self):
        return self.__pillar

    def make_encapsulation(self):
        self.__pillar = Encapsulation()
        self.__monster = Ogre()

    def make_polymorphism(self):
        self.__pillar = Polymorphism()
        self.__monster = Ogre()

    def make_inheritance(self):
        self.__pillar = Inheritance()
        self.__monster = Ogre()

    def make_abstraction(self):
        self.__pillar = Abstraction()
        self.__monster = Ogre()

    def discard_pillar(self):
        self.__pillar = None

    # -------- Potion --------- #
    @property
    def potion(self):
        return self.__potion

    def generate_potion(self):
        if random.randint(0, 100) < 10:
            self.random_potion()

    def random_potion(self):
        if random.randint(0, 100) < 50:
            self.health_potion()
        else:
            self.vision_potion()

    def health_potion(self):
        self.__potion = Health_Potion

    def vision_potion(self):
        self.__potion = Vision_Potion

    def dicard_potioon(self):
        self.__potion = None

    # -------- Pit ----------- #
    @property
    def pit(self):
        return self.__pit

    def generate_pit(self):
        if random.randint(0, 100) < 10:
            self.make_pit()

    def make_pit(self):
        self.__pit = random.randint(1, 20)

    def discard_pit(self):
        self.__pit = None

    # ------------ entrance and exit ----------- #
    def make_entrance(self):
        self.__entrance = self.__location

    @property
    def entrance(self):
        return self.__entrance

    def make_exit(self):
        self.__exit = self.__location

    @property
    def exit(self):
        return self.__exit

    ## Monsters ##

    @property
    def monster(self):
        return self.__monster

    def monster_defeated(self):
        self.__monster = None

    def generate_monster(self):
        if random.randint(0, 100) <= 1000: #change it to 75
            self.make_monster()

    def make_monster(self):
        chance = random.randint(0, 100)
        if chance <= 33:
            self.__monster = Gremlin()
        elif chance <= 66:
            self.__monster = Skeleton()
        else:
            self.__monster = Ogre()

        self.__monster.position = self.__location

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
        # String = self.north() + "\n"
        # String = String + self.center() + "\n"
        # String = String + self.south() + "\n"
        # return String
        self.stat()

    # Room stats #

    def stat(self):
        return f"potion: {self.potion} \n monster: {self.monster} \n pit: {self.pit} \n pillar: {self.pillar}\n" \
               f"entrance: {self.entrance} \n exit: {self.exit} \n location: {self.__location}"

# room = Room()
# room.generate("I", (0, 0))
# room.stat()
