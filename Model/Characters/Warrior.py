import random

from Model.Characters.Heroes import Hero
from Model.Characters.DungeonCharacter import DungeonCharacter


class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name, health=125, min_damage=35, max_damage=60, attack_speed=4, chance_to_hit=0.8,
                         chance_to_block=0.2)

    def special_skill(self, target):
        # Implement the heal special skill
        crushing_blow = random.randint(75, 175)  # Adjust the healing range as needed
        percent = 40
        if random.randint(0, 100) <= 40:
            self.crushing_blow(crushing_blow, opponent=DungeonCharacter)
            return f"{self._name} used crushing blow on {target.name}, dealing {crushing_blow} damage."
        else:
            return f"{self._name} used crushing blow on {target.name}, but missed."

    def crushing_blow(self, special, opponent = DungeonCharacter):
        opponent.receive_damage(self, special)

# Example usage:
# priestess = Priestess("PriestessName")

