import sqlite3
from Model.Characters.Monsters.Monster import Monster
import random


class Gremlin(Monster):
    """
    Represents a Gremlin monster in the game.

    The Gremlin is a specific type of Monster with attributes and behaviors defined in the database.
    It inherits from the Monster class and extends it with specific attack logic and data fetching from a database.

    The data for the Gremlin, such as name, health, and attack parameters, are fetched from a SQLite database.
    """

    def __init__(self):
        """
        Initializes a Gremlin monster by fetching its data from the database and setting up its attributes.
        """
        gremlin_data = Gremlin.fetch_gremlin_data()
        name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal = gremlin_data
        super().__init__(name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal)

    def attack(self, opponent):
        """
        Execute an attack on an opponent.

        The Gremlin performs an attack that inflicts random damage within its damage range. After attacking,
        the Gremlin has a chance to heal itself.

        :param opponent: The DungeonCharacter object representing the opponent being attacked.
        """
        if self.can_attack():
            damage = random.randint(self._min_damage, self._max_damage)
            opponent.receive_damage(damage)
            print(f"{self._name} attacked {opponent.name} for {damage} damage.")
            self.heal()
        else:
            print(f"{self._name} missed the attack on {opponent.name}.")

    @staticmethod
    def fetch_gremlin_data():
        """
        Fetch the Gremlin's data from the database.

        Retrieves the Gremlin's attributes such as name, health, and attack parameters from a SQLite database.

        :return:the Gremlin's data.
        """
        # connection = sqlite3.connect("../../db/monsters.db")
        connection = sqlite3.connect("/Users/billy/2023-2024/Fall/360/LegendOfDub/Model/db/monsters.db")
        cur = connection.cursor()

        cur.execute("SELECT * FROM monster WHERE monster_type = 'Gremlin'")
        gremlin_data = cur.fetchone()

        connection.close()
        return gremlin_data

# Example of instantiating a Gremlin
# gremlin = Gremlin()
# print(gremlin)
