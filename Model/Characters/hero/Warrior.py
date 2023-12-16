
from Model.Characters.hero.Heroes import Hero
import random

class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name, health=125, min_damage=35, max_damage=60, attack_speed=4, chance_to_hit=0.8, chance_to_block=0.2)

    def special_skill(self, opponent):
        # Implement the Crushing Blow special skill
        if random.random() <= 0.4:  # 40% chance of success
            damage = random.randint(75, 175)
            opponent.receive_damage(damage)
            print(f"{self.get_name()} used Crushing Blow on {opponent.get_name()} for {damage} damage.")
        else:
            print(f"{self.get_name()} attempted Crushing Blow on {opponent.get_name()} but missed.")