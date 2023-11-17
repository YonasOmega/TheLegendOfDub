from Model.Characters.Monster import Monster
import random

class Skeleton(Monster):
    def __init__(self, name="Skeleton"):
        super().__init__(name, health=100, min_damage=30, max_damage=50, attack_speed=3, chance_to_hit=0.8, chance_to_heal=0.3)

    def attack(self, opponent):
        if self.can_attack():
            damage = random.randint(self._min_damage, self._max_damage)
            opponent.receive_damage(damage)
            print(f"{self._name} attacked {opponent.name} for {damage} damage.")
            self.heal()  # The Skeleton has a chance to heal after any attack
        else:
            print(f"{self._name} missed the attack on {opponent.name}.")

