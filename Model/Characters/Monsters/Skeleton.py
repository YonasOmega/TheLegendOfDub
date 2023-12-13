import sqlite3
from Model.Characters.Monsters.Monster import Monster
import random

class Skeleton(Monster):
    def __init__(self):
        skeleton_data = Skeleton.fetch_skeleton_data()
        name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal = skeleton_data
        super().__init__(name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal)


    @staticmethod
    def fetch_skeleton_data():
        try:
            #connection = sqlite3.connect("../../db/monsters.db")
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
