import random
from Model.Characters.Heroes import Hero
from Model.Characters.DungeonCharacter import DungeonCharacter


class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name, health=75, min_damage=20, max_damage=40, attack_speed=6, chance_to_hit=0.8,
                         chance_to_block=0.4)

    def special_skill(self, opponent: DungeonCharacter):
        # Implement surprise attack special skill
        surprise_attack_chance = random.randint(0, 100)
        if surprise_attack_chance <= 20:
            return f"{self._name} attempted a sneak attack on {opponent.get_name()}, but got caught."
        elif surprise_attack_chance <= 60:
            damage = self.attack(opponent)
            return f"{self._name} used a sneak attack on {opponent.get_name()}, resulting in a normal attack of {damage}"
        else:
            # Increase damage for a successful surprise attack
            self.attack(opponent)
            return f"{self._name} successfully executed a sneak attack on {opponent.get_name()}."

    def attack(self, opponent):
        # Utilize the perform_attack method from the parent class
        return opponent.receive_damage(self.calculate_damage())
