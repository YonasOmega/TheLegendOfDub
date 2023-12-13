import sqlite3
from Model.Characters.Monsters.Monster import Monster
import random
import os


class Gremlin(Monster):
    def __init__(self):
        print("WOrking directory: ", os.getcwd())
        gremlin_data = Gremlin.fetch_gremlin_data()
        name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal = gremlin_data
        super().__init__(name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal)

    @staticmethod
    def fetch_gremlin_data():
        db_path = os.path.join(os.getcwd(), "Model", "db", "monsters.db")
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

# Example of instantiating a Gremlin
# gremlin = Gremlin()
# print(gremlin)
