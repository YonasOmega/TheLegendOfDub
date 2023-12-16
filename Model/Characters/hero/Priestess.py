import random

from Model.Characters.hero.Heroes import Hero


class Priestess(Hero):
    def __init__(self, name):
        super().__init__(name, health=75, min_damage=25, max_damage=45, attack_speed=5, chance_to_hit=0.7, chance_to_block=0.3)

    def special_skill(self, target):
        # Implement the heal special skill
        heal_amount = random.randint(15, 30)  # Adjust the healing range as needed
        self.receive_healing(heal_amount)
        print(f"{self.get_name()} healed back {heal_amount} hit points.")

    def receive_healing(self, amount):
        self.set_health(amount)
