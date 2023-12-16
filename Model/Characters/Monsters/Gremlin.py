import sqlite3
from Model.Characters.Monsters.Monster import Monster

class Gremlin(Monster):
    """
    Gremlin class represents a specific type of monster - a Gremlin, inheriting from Monster.
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
        Fetches Gremlin data from the database.

        Returns:
            tuple: A tuple containing Gremlin data (name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal).
        """
        # Adjust the database path as needed
        connection = sqlite3.connect("/Users/billy/2023-2024/Fall/360/LegendOfDub/Model/db/monsters.db")
        cur = connection.cursor()

        cur.execute("SELECT * FROM monster WHERE monster_type = 'Gremlin'")
        gremlin_data = cur.fetchone()

        connection.close()
        return gremlin_data

# Example of instantiating a Gremlin
# gremlin = Gremlin()
# print(gremlin)
