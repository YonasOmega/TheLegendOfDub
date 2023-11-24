from Model.Characters.Monsters.Monster import Monster
import random

class Ogre(Monster):
    def __init__(self, name="Ogre"):
        super().__init__(name, health=200, min_damage=30, max_damage=60, attack_speed=2, chance_to_hit=0.6, chance_to_heal=0.1)

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
