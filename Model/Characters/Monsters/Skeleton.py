import sqlite3
from Model.Characters.Monsters.Monster import Monster
import random

class Skeleton(Monster):
    """
    Represents a Skeleton monster in the game.

    The Skeleton is a specific type of Monster with attributes and behaviors defined in the database.
    It inherits from the Monster class and extends it with specific attack logic and data fetching from a database.

    The data for the Skeleton, such as name, health, and attack parameters, are fetched from a SQLite database.
    """
    def __init__(self):
        """
        Initializes a Skeleton monster by fetching its data from the database and setting up its attributes.
        """
        skeleton_data = Skeleton.fetch_skeleton_data()
        name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal = skeleton_data
        super().__init__(name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal)

    def attack(self, opponent):
        """
        Execute an attack on an opponent.

        The Skeleton performs an attack that inflicts random damage within its damage range. After attacking,
        the Skeleton has a chance to heal itself.

        :param opponent: The DungeonCharacter object representing the opponent being attacked.
        """
        if self.can_attack():
            damage = random.randint(self._min_damage, self._max_damage)
            opponent.receive_damage(damage)
            print(f"{self._name} attacked {opponent.name} for {damage} damage.")
            self.heal()
        else:
            print(f"{self._name} missed the attack on {opponent.name}.")

    # @staticmethod
    # def fetch_skeleton_data():
    #     connection = sqlite3.connect("../../db/monsters.db")
    #     cur = connection.cursor()
    #
    #     cur.execute("SELECT * FROM monster WHERE monster_type = 'Skeleton'")
    #     skeleton_data = cur.fetchone()
    #
    #     connection.close()
    #     return skeleton_data
    @staticmethod
    def fetch_skeleton_data():
        """
        Fetch the Skeleton's data from the database.

        Retrieves the Skeleton's attributes such as name, health, and attack parameters from a SQLite database.
        Includes error handling for database connection and querying issues.

        :return:the Skeleton's data, or None if an error occurred.
        """
        try:
            #connection = sqlite3.connect("../../db/monsters.db")
            connection = sqlite3.connect("/Users/billy/2023-2024/Fall/360/LegendOfDub/Model/db/monsters.db")
        except sqlite3.OperationalError as e:
            print(f"Error opening database: {e}")
            return None

        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM monster WHERE monster_type = 'Skeleton'")
            skeleton_data = cur.fetchone()
        except sqlite3.OperationalError as e:
            print(f"Error querying database: {e}")
            skeleton_data = None

        connection.close()
        return skeleton_data


# Example of instantiating a Skeleton
# skeleton = Skeleton()
# print(skeleton)
