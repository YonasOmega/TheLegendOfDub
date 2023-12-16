from abc import ABC
import sqlite3

from Model.Characters.DungeonCharacter import DungeonCharacter
import random
import os


class Monster(DungeonCharacter, ABC):
    """
    Represents a monster in the dungeon game, inheriting from DungeonCharacter.
    Includes additional functionality for healing during combat.
    """
    def __init__(self, name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal):
        """
        Initializes a Monster instance with given attributes.

        Parameters:
            - name (str): The name of the monster.
            - health (int): Health points of the monster.
            - min_damage (int): Minimum damage the monster can inflict.
            - max_damage (int): Maximum damage the monster can inflict.
            - attack_speed (float): Attack speed of the monster.
            - chance_to_hit (float): Probability of a successful attack.
            - chance_to_heal (float): Probability of healing after receiving damage.
        """
        super().__init__(name, health, min_damage, max_damage, attack_speed, chance_to_hit)
        self.__chance_to_heal = chance_to_heal

    @property
    def chance_to_heal(self):
        return self.__chance_to_heal

    @chance_to_heal.setter
    def chance_to_heal(self, value):
        self.__chance_to_heal = value

    def heal(self):
        """
        Handles the monster's self-healing mechanism after receiving damage.
        """
        # A Monster has a chance to heal after any attack that causes a loss of hit points
        # The chance to heal is checked after the Monster has been attacked and hit points have been lost
        if self.is_alive() and random.random() < self.__chance_to_heal:
            heal_amount = random.randint(15, 30)  # Adjust the healing range as needed
            self.set_health(heal_amount)
            print(f"{self.get_name()} healed itself for {heal_amount} hit points.")

    def attack(self, opponent):
        """
        Conducts an attack on the opponent.

        Parameters:
            - opponent (DungeonCharacter): The character to attack.
        """
        if self.can_attack():
            damage = random.randint(self.min_damage, self.max_damage)
            print(f"{self.get_name()} attacked {opponent.get_name()} for {damage} damage.")
            opponent.receive_damage(damage)
            self.heal()
        else:
            print(f"{self.get_name()} missed the attack on {opponent.get_name()}.")


class Gremlin(Monster):
    """
    Represents a Gremlin monster, inheriting from Monster.
    Fetches its unique attributes from a database.
    """
    def __init__(self):
        """
        Initializes a Gremlin instance with data fetched from the database.
        """
        gremlin_data = Gremlin.fetch_gremlin_data()
        name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal = gremlin_data
        super().__init__(name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal)

    @staticmethod
    def fetch_gremlin_data():
        """
        Fetches data for a Gremlin from the database.

        Returns:
            tuple: Containing the data attributes for the Gremlin.
        """
        db_path = os.path.join(os.path.dirname(os.getcwd()), "Model", "db", "monsters.db")
        try:
            connection = sqlite3.connect(db_path)
        except sqlite3.OperationalError as e:
            print(f"Error opening database: {e}")
            return None

        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM monster WHERE monster_type = 'Gremlin'")
            monster_data = cur.fetchone()
        except sqlite3.OperationalError as e:
            print(f"Error querying database: {e}")
            monster_data = None

        connection.close()
        return monster_data


class Skeleton(Monster):
    """
    Represents a Skeleton monster, inheriting from Monster.
    Fetches its unique attributes from a database.
    """

    def __init__(self):
        """
        Initializes a Skeleton instance with data fetched from the database.
        """
        skeleton_data = Skeleton.fetch_skeleton_data()
        name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal = skeleton_data
        super().__init__(name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal)

    @staticmethod
    def fetch_skeleton_data():
        """
        Fetches data for a Skeleton from the database.

        Returns:
            tuple: Containing the data attributes for the Skeleton.
        """
        db_path = os.path.join(os.path.dirname(os.getcwd()), "Model", "db", "monsters.db")
        try:
            connection = sqlite3.connect(db_path)
        except sqlite3.OperationalError as e:
            print(f"Error opening database: {e}")
            return None

        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM monster WHERE monster_type = 'Skeleton'")
            monster_data = cur.fetchone()
        except sqlite3.OperationalError as e:
            print(f"Error querying database: {e}")
            monster_data = None

        connection.close()
        return monster_data


class Ogre(Monster):
    """
    Represents a Ogre monster, inheriting from Monster.
    Fetches its unique attributes from a database.
    """

    def __init__(self):
        """
        Initializes a Ogre instance with data fetched from the database.
        """
        ogre_data = Ogre.fetch_ogre_data()
        name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal = ogre_data
        super().__init__(name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal)

    @staticmethod
    def fetch_ogre_data():
        """
        Fetches data for an Ogre from the database.

        Returns:
            tuple: Containing the data attributes for the Ogre.
        """
        db_path = os.path.join(os.path.dirname(os.getcwd()), "Model", "db", "monsters.db")
        try:
            connection = sqlite3.connect(db_path)
        except sqlite3.OperationalError as e:
            print(f"Error opening database: {e}")
            return None

        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM monster WHERE monster_type = 'Ogre'")
            monster_data = cur.fetchone()
        except sqlite3.OperationalError as e:
            print(f"Error querying database: {e}")
            monster_data = None

        connection.close()
        return monster_data
