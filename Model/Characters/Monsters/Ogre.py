import sqlite3
from Model.Characters.Monsters.Monster import Monster
import random


class Ogre(Monster):
    """
    Represents an Ogre monster in the game.

    The Ogre is a specific type of Monster with attributes and behaviors defined in the database.
    It inherits from the Monster class and extends it with specific attack logic and data fetching from a database.

    The data for the Ogre, such as name, health, and attack parameters, are fetched from a SQLite database.
    """
    def __init__(self):
        """
        Initializes an Ogre monster by fetching its data from the database and setting up its attributes.
        """
        ogre_data = Ogre.fetch_ogre_data()
        name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal = ogre_data
        super().__init__(name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal)

    def attack(self, opponent):
        """
        Execute an attack on an opponent.

        The Ogre performs an attack that inflicts random damage within its damage range. After attacking,
        the Ogre has a chance to heal itself.

        :param opponent: The DungeonCharacter object representing the opponent being attacked.
        """
        # Optionally, you can override the attack method for the Ogre's specific attack behavior
        if self.can_attack():
            damage = random.randint(self._min_damage, self._max_damage)
            opponent.receive_damage(damage)
            print(f"{self._name} attacked {opponent.name} for {damage} damage.")
            self.heal()  # The Ogre has a chance to heal after any attack
        else:
            print(f"{self._name} missed the attack on {opponent.name}.")

    # Optionally, you can add more methods or override existing ones as needed for Ogre-specific behavior

    @staticmethod
    def fetch_ogre_data():
        """
        Fetch the Ogre's data from the database.

        Retrieves the Ogre's attributes such as name, health, and attack parameters from a SQLite database.

        :return:the Ogre's data.
        """
        #connection = sqlite3.connect("../../db/monsters.db")
        connection = sqlite3.connect("/Users/billy/2023-2024/Fall/360/LegendOfDub/Model/db/monsters.db")
        cur = connection.cursor()

        cur.execute("SELECT * FROM monster WHERE monster_type = 'Ogre'")
        ogre_data = cur.fetchone()

        connection.close()
        return ogre_data

#
# ogre = Ogre()
# print(ogre)
