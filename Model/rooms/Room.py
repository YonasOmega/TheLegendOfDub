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
    """
    Represents a room within a dungeon, with various elements like potions, pits, monsters, and pillars.

    Attributes:
        __potion (Potion): An instance of a potion present in the room.
        __pit (int): The damage value of a pit if present in the room.
        __entrance (tuple): The coordinates of the entrance if present.
        __exit (tuple): The coordinates of the exit if present.
        __doors (list): A list of doors in the room, represented as cardinal directions.
        __monster (Monster): An instance of a monster present in the room.
        __pillar (Pillar): An instance of a pillar present in the room.
        __location (tuple): The coordinates of the room within the dungeon.
    """
    def __init__(self, location: tuple):
        """
        Initializes a Room instance.

        :parameter:
            location (tuple): The coordinates of the room within the dungeon.
        """

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
        Generates room content based on the provided special character.

        :parameter:
            special (str): A character representing the type of content in the room.
        """
        self.generate_special(special)

    def generate_non_special(self):
        """
        Generates standard contents for a non-special room, including potions and monsters.
        """
        self.generate_potion()
        self.generate_pit()
        self.generate_monster()

    def generate_pillar(self, special: str):
        """
        Generates a specific pillar and monster for the room based on the pillar type.

        :parameter:
            special (str): A character representing the type of pillar.
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

    def generate_special(self, special: str):
        """
        Generates special elements for the room such as entrance, exit, and pillars.

        Args:
            special (str): A character representing the special element in the room.
        """
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
        """
        Returns the pillar object in the room, if any.
        """
        return self.__pillar

    def make_encapsulation(self):
        """
        Makes the encapsulation pillar
        """
        self.__pillar = Encapsulation()
        self.__monster = Ogre()

    def make_polymorphism(self):
        """
        Makes the polymorphism pillar
        """
        self.__pillar = Polymorphism()
        self.__monster = Ogre()

    def make_inheritance(self):
        """
        Makes the inheritance pillar
        """
        self.__pillar = Inheritance()
        self.__monster = Ogre()

    def make_abstraction(self):
        """
        Makes the abstraction pillar
        """
        self.__pillar = Abstraction()
        self.__monster = Ogre()

    def discard_pillar(self):
        """
        Discards a pillar. Should be used when Player picks up a pillar
        """
        self.__pillar = None

    # -------- Potion --------- #
    @property
    def potion(self):
        """
        Returns a potion, if any
        """
        return self.__potion

    def generate_potion(self):
        """
        Generates a potion associated to the room
        """
        if random.randint(0, 100) < 10:
            self.random_potion()

    def random_potion(self):
        """
        Makes the potion a health or vision
        """
        if random.randint(0, 100) < 50:
            self.health_potion()
        else:
            self.vision_potion()

    def health_potion(self):
        """
        Set's a potion to be a health potion
        """
        self.__potion = Health_Potion

    def vision_potion(self):
        """
        Set's a potion to be a vision potion
        """
        self.__potion = Vision_Potion

    def dicard_potioon(self):
        """
        Discard's a potion, used when player picks up potion
        """
        self.__potion = None

    # -------- Pit ----------- #
    @property
    def pit(self):
        """
        Returns a pit
        """
        return self.__pit

    def generate_pit(self):
        """
        Generates a pit
        """
        if random.randint(0, 100) < 10:
            self.make_pit()

    def make_pit(self):
        """
        Give's a pit a damage value
        """
        self.__pit = random.randint(1, 20)

    def discard_pit(self):
        """
        Discard's a pit, after player encounters and takes damage
        """
        self.__pit = None

    # ------------ entrance and exit ----------- #
    def make_entrance(self):
        """
        Marks the room as the entrance of the dungeon.
        """
        self.__entrance = self.__location

    @property
    def entrance(self):
        """
        Gets the location of the entrance if the room is marked as an entrance.

        Returns:
            tuple or None: The coordinates of the entrance or None if not an entrance.
        """
        return self.__entrance

    def make_exit(self):
        """
        Marks the room as the exit of the dungeon.
        """
        self.__exit = self.__location

    @property
    def exit(self):
        """
        Gets the location of the exit if the room is marked as an exit.

        Returns:
            tuple or None: The coordinates of the exit or None if not an exit.
        """
        return self.__exit

    ## Monsters ##

    @property
    def monster(self):
        """
        Gets the monster present in the room, if any.

        Returns:
            Monster or None: The monster object or None if no monster is present.
        """
        return self.__monster

    def monster_defeated(self):
        """
        Marks the monster in the room as defeated, effectively removing it.
        """
        self.__monster = None

    def generate_monster(self):
        """
        Randomly generates a monster in the room based on a specified probability.
        """
        if random.randint(0, 100) <= 1000: #change it to 75
            self.make_monster()

    def make_monster(self):
        """
        Randomly selects and creates a specific type of monster (Gremlin, Skeleton, or Ogre) in the room.
        """
        chance = random.randint(0, 100)
        if chance <= 33:
            self.__monster = Gremlin()
        elif chance <= 66:
            self.__monster = Skeleton()
        else:
            self.__monster = Ogre()

        self.__monster.position = self.__location

    def __str__(self):
        """
        Overrides the default string representation to provide a summary of the room's contents and status.

        Returns:
            str: A string representation of the room, including its status and contents.
        """
        self.stat()

    # Room stats #

    def stat(self):
        """
        Generates a detailed status report of the room, including information about any potions, monsters, pits, pillars, entrance, and exit present.

        Returns:
            str: A multiline string containing details about the room's contents and features.
        """
        return f"potion: {self.potion} \n monster: {self.monster} \n pit: {self.pit} \n pillar: {self.pillar}\n" \
               f"entrance: {self.entrance} \n exit: {self.exit} \n location: {self.__location}"

# room = Room()
# room.generate("I", (0, 0))
# room.stat()
