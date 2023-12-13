from abc import ABC

from Model.Characters.DungeonCharacter import DungeonCharacter
import random


class Monster(DungeonCharacter, ABC):
    def __init__(self, name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal):
        super().__init__(name, health, min_damage, max_damage, attack_speed, chance_to_hit)
        # self._position = (0,0)
        self._chance_to_heal = chance_to_heal

    @property
    def chance_to_heal(self):
        return self._chance_to_heal

    @chance_to_heal.setter
    def chance_to_heal(self, value):
        self._chance_to_heal = value

    def move(self):
        # Implement the logic for Monster movement here
        print(f"{self._name} is moving.")

    def heal(self):
        # A Monster has a chance to heal after any attack that causes a loss of hit points
        # The chance to heal is checked after the Monster has been attacked and hit points have been lost
        if self.is_alive() and random.random() < self._chance_to_heal:
            heal_amount = random.randint(15, 30)  # Adjust the healing range as needed
            self._health += heal_amount
            print(f"{self._name} healed itself for {heal_amount} hit points.")

    def attack(self, opponent):
        if self.can_attack():
            damage = random.randint(self._min_damage, self._max_damage)
            print(f"{self._name} attacked {opponent._name} for {damage} damage.")
            opponent.receive_damage(damage)
            self.heal()
        else:
            print(f"{self._name} missed the attack on {opponent._name}.")
