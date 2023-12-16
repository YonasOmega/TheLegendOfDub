import sqlite3
from Model.Characters.Monsters.Monster import Monster

class Skeleton(Monster):
    """
    Skeleton class represents a specific type of monster - a Skeleton, inheriting from Monster.
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
        Fetches Skeleton data from the database.

        Returns:
            tuple: A tuple containing Skeleton data (name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal).
        """
        try:
            # Adjust the database path as needed
            connection = sqlite3.connect("/Users/billy/2023-2024/Fall/360/TheLegendOfDub/Model/db/monsters.db")
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
