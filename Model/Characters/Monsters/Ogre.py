import sqlite3
from Model.Characters.Monsters.Monster import Monster
import random


class Ogre(Monster):
    def __init__(self):
        ogre_data = Ogre.fetch_ogre_data()
        name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal = ogre_data
        super().__init__(name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal)

    def attack(self, opponent):
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
        connection = sqlite3.connect("../../db/monsters.db")
        #connection = sqlite3.connect("/Users/billy/2023-2024/Fall/360/LegendOfDub/Model/db/monsters.db")
        cur = connection.cursor()

        cur.execute("SELECT * FROM monster WHERE monster_type = 'Ogre'")
        ogre_data = cur.fetchone()

        connection.close()
        return ogre_data

#
# ogre = Ogre()
# print(ogre)
