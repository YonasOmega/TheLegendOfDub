import sqlite3
from Model.Characters.Monsters.Monster import Monster
import random

class Gremlin(Monster):
    def __init__(self):
        gremlin_data = Gremlin.fetch_gremlin_data()
        name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal = gremlin_data
        super().__init__(name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal)

    def attack(self, opponent):
        if self.can_attack():
            damage = random.randint(self._min_damage, self._max_damage)
            opponent.receive_damage(damage)
            print(f"{self._name} attacked {opponent.name} for {damage} damage.")
            self.heal()
        else:
            print(f"{self._name} missed the attack on {opponent.name}.")

    @staticmethod
    def fetch_gremlin_data():
        connection = sqlite3.connect("../../db/monsters.db")
        cur = connection.cursor()

        cur.execute("SELECT * FROM monster WHERE monster_type = 'Gremlin'")
        gremlin_data = cur.fetchone()

        connection.close()
        return gremlin_data

# Example of instantiating a Gremlin
gremlin = Gremlin()
print(gremlin)
