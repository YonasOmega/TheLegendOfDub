from Model.Characters.Monster import Monster
import random

class Gremlin(Monster):
    def __init__(self, name="Gremlin"):
        super().__init__(name, health=70, min_damage=15, max_damage=30, attack_speed=5, chance_to_hit=0.8, chance_to_heal=0.4)

    def attack(self, opponent):
        # can override the attack method for the Gremlin's specific attack behavior
        if self.can_attack():
            damage = random.randint(self._min_damage, self._max_damage)
            opponent.receive_damage(damage)
            print(f"{self._name} attacked {opponent.name} for {damage} damage.")
            self.heal()  # The Gremlin has a chance to heal after any attack
        else:
            print(f"{self._name} missed the attack on {opponent.name}.")

