from Model.Characters.hero.Heroes import Hero
import random

class Thief(Hero):
    def __init__(self, name):
        super().__init__(name, health=75, min_damage=20, max_damage=40, attack_speed=6, chance_to_hit=0.8, chance_to_block=0.4)

    def special_skill(self, opponent):
        # Implement the Surprise Attack special skill
        skill_result = random.random()

        if skill_result < 0.4:  # 40% chance of successful surprise attack
            damage = random.randint(self._min_damage, self._max_damage)
            opponent.receive_damage(damage)
            return f"{self._name} successfully performed a surprise attack on {opponent.name} for {damage} damage and gets an extra turn."
        elif skill_result < 0.6:  # 20% chance of getting caught
            return f"{self._name} attempted a surprise attack but got caught. No attack this round."
        else:  # 40% chance of a normal attack
            damage = random.randint(self._min_damage, self._max_damage)
            opponent.receive_damage(damage)
            return f"{self._name} performed a normal attack on {opponent.name} for {damage} damage."

    # Optionally, you can override the attack method if the Thief's attack behavior is different.
    # def attack(self, opponent):
    #     # Custom implementation for Thief's attack if needed
    #     pass


