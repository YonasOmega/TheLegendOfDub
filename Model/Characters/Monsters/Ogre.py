import sqlite3
from Model.Characters.Monsters.Monster import Monster


class Ogre(Monster):
    """
    Ogre class represents a specific type of monster - an Ogre, inheriting from Monster.
    """

    def __init__(self):
        """
        Initializes an Ogre instance with data fetched from the database.
        """
        ogre_data = Ogre.fetch_ogre_data()
        name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal = ogre_data
        super().__init__(name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal)

    @staticmethod
    def fetch_ogre_data():
        """
        Fetches Ogre data from the database.

        Returns:
            tuple: A tuple containing Ogre data (name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal).
        """
        # Adjust the database path as needed
        connection = sqlite3.connect("/Users/billy/2023-2024/Fall/360/LegendOfDub/Model/db/monsters.db")
        cur = connection.cursor()

        cur.execute("SELECT * FROM monster WHERE monster_type = 'Ogre'")
        ogre_data = cur.fetchone()

        connection.close()
        return ogre_data
