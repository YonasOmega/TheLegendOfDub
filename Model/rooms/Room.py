import random
import sqlite3

from Model.rooms.Items.potion.Health_Potion import Health_Potion
from Model.rooms.Items.potion.Vision_Potion import Vision_Potion
from Model.Characters.Monsters.Ogre import Ogre
from Model.Characters.Monsters.Skeleton import Skeleton
from Model.Characters.Monsters.Gremlin import Gremlin
from Model.rooms.Items.Pillar.OOP import Polymorphism
from Model.rooms.Items.Pillar.OOP import Encapsulation
from Model.rooms.Items.Pillar.OOP import Inheritance
from Model.rooms.Items.Pillar.OOP import Abstraction


class Room:
    """
    Represents a room in our 2d-dungeon game.

    The room can contain various elements like potions, a pit, an entrance, an exit, doors, a monster, and or a pillar.
    Each room has a specific location within a dungeon.

     Attributes:
        __potion (Potion): A potion present in the room, can be either a Health or Vision potion.
        __pit (int): A pit present in the room means the player falls and takes damage.
        __entrance (tuple): The location of the entrance if this room is the entrance.
        __exit (tuple): The location of the exit if this room is the exit.
        __doors (list): List of doors in the room: North, East, South, West
        __monster (Monster): The monster present in the room. A monster can be Ogre, Gremlin, or Skeleton.
        __pillar (Pillar): One of the OOP pillars present in the room.
        __location (tuple): The coordinates of the room in the dungeon.
    """

    def __init__(self, location: tuple):
        """
        Initialize the room with a specific location.

        :param location: A tuple representing the coordinates of the room in the Dungeon.
        :type location: tuple

        :raises ValueError: If the location is not a tuple of two integers or the integers are less than 0.
        """
        # Check if location is a tuple
        if not isinstance(location, tuple):
            raise ValueError("Location must be a tuple")

        # Check if the tuple has two elements
        if len(location) != 2:
            raise ValueError("Location must have two elements")

        # Check if both elements in the tuple are integers and greater than or equal to 0
        if not all(isinstance(coord, int) and coord >= 0 for coord in location):
            raise ValueError("Both elements of the location must be integers greater than or equal to 0")

        self.__potion = None
        self.__pit = None
        self.__entrance = None
        self.__exit = None
        self.__doors = list()
        self.__monster = None
        self.__pillar = None
        self.__location = location

    def generate(self, special: str):
        """
        Generates the attributes for the room based on the "special" string parameter.
        The string parameter will come from the DungeonGenerator.
        0: Room doesn't exist.
        1: Room is a Path.
        X: Room is an entrance.
        Y: Room is an Exit.
        A: Room contains the Abstraction pillar.
        E: Room contains the Encapsulation pillar.
        P: Room contains the Polymorphism pillar.
        I: Room contains the Inheritance pillar.

        :param special: A string indicating the type of room it is in the dungeon.
        :type special: str

        :return: Void
        """
        self.generate_special(special)

    def generate_special(self, special: str):
        """
        Helper class to make generate method simpler.

        :param special: A string indicating the type of room it is in the dungeon.
        :type special: str

        :return: Void
        """
        if special == "X":
            self.make_entrance()
        elif special == "Y":
            self.make_exit()
        elif special == "1":
            self.generate_non_special()
        elif special != "0":
            self.generate_pillar(special)

    def generate_non_special(self):
        """
        Generates the attributes for a non-special Room.
        A non-special room would mean that the special string was a 1.
        Would give self.__potion, self.__pit, and self.__monster a chance to be giving a value.

        :return: Void
        """
        self.generate_potion()
        self.generate_pit()
        self.generate_monster()

    def generate_pillar(self, special: str):
        """
        Generates the attributes for a Pillar room. This would also make self.__monster an Ogre

        :param special: A string, either an "E", "P", "I", or "A".
        :type special: str

        :return: Void
        """
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



    # -------- Pillar ---------#
    @property
    def pillar(self):
        """
        returns self.__pillar

        :return: self.__pillar
        """
        return self.__pillar

    def make_encapsulation(self):
        """
        Makes the room a pillar room for the Encapsulation pillar.

        :return: Void
        """
        self.__pillar = Encapsulation()
        self.__monster = Ogre()

    def make_polymorphism(self):
        """
        Makes the room a pillar room for the Polymorphism pillar.

        :return: Void
        """
        self.__pillar = Polymorphism()
        self.__monster = Ogre()

    def make_inheritance(self):
        """
        Makes the room a pillar room for the Inheritance pillar.

        :return: Void
        """
        self.__pillar = Inheritance()
        self.__monster = Ogre()

    def make_abstraction(self):
        """
        Makes the room a pillar room for the Abstraction pillar.

        :return: Void
        """
        self.__pillar = Abstraction()
        self.__monster = Ogre()

    # -------- Potion --------- #
    @property
    def potion(self):
        """
        Returns self.__potion.

        :return: self.__potion
        """
        return self.__potion

    def generate_potion(self):
        """
        A 10% chance that a potion gets generated for a room.

        :return: Void
        """
        if random.randint(0, 100) < 10:
            self.random_potion()

    def random_potion(self):
        """
        Either makes the potion a health potion or a vision potion.

        :return: Void
        """
        if random.randint(0, 100) < 50:
            self.health_potion()
        else:
            self.vision_potion()

    def health_potion(self):
        """
        Makes potion a health potion.

        :return: Void
        """
        self.__potion = Health_Potion

    def vision_potion(self):
        """
        Makes potion a vision potion.

        :return: Void
        """
        self.__potion = Vision_Potion

    # -------- Pit ----------- #
    @property
    def pit(self):
        """
        Returns self.__pit

        :return: self.__pit
        """
        return self.__pit

    def generate_pit(self):
        """
        A 10% chance that a pit gets generated

        :return: Void
        """
        if random.randint(0, 100) < 10:
            self.make_pit()

    def make_pit(self):
        """
        Gives the damage value for a pit from 1-20

        :return: Void
        """
        self.__pit = random.randint(1, 20)

    # ------------ entrance and exit ----------- #
    @property
    def entrance(self):
        """
        Returns the location of the entrance

        :return: self.__entrance
        """
        return self.__entrance

    def make_entrance(self):
        """
        Sets the location for the entrance.

        :return: void
        """
        self.__entrance = self.__location

    @property
    def exit(self):
        """
        Returns the location of the exit.

        :return: self.__exit
        """
        return self.__exit

    def make_exit(self):
        """
        Sets the location for the exit.

        :return: Void
        """
        self.__exit = self.__location

    ## Monsters ##
    @property
    def monster(self):
        """
        Returns the monster.

        :return: self.__monster
        """
        return self.__monster

    def generate_monster(self):
        """
        a 75% chance that a monster generates.

        :return: Void
        """
        if random.randint(0, 100) <= 75:
            self.make_monster()

    def make_monster(self):
        """
        1/3 chance for making a monster a gremlin,
        1/3 chance for making a monster a Skeleton,
        1/3 chance for making a monster an Ogre.

        :return: Void
        """
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
        """
        A string representation of Room class

        :return: string representation of a room.
        """
        # String = self.north() + "\n"
        # String = String + self.center() + "\n"
        # String = String + self.south() + "\n"
        # return String
        self.stat()

    # Room stats #

    def stat(self):
        """
        Returns the attributes of the room.
        :return: Room attributes.
        """
        return f"potion: {self.potion} \n monster: {self.monster} \n pit: {self.pit} \n pillar: {self.pillar}\n" \
               f"entrance: {self.entrance} \n exit: {self.exit} \n location: {self.__location}"

# room = Room()
# room.generate("I", (0, 0))
# room.stat()
