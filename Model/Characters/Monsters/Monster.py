from abc import ABC

from Model.Characters.DungeonCharacter import DungeonCharacter
import random


class Monster(DungeonCharacter, ABC):
    """
    Monster class represents a creature in a dungeon-based game, inheriting from DungeonCharacter.
    """

    def __init__(self, name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal):
        """
        Initializes a Monster with the specified attributes.

        Parameters:
            - name (str): The name of the monster.
            - health (int): The initial health points of the monster.
            - min_damage (int): The minimum damage the monster can inflict.
            - max_damage (int): The maximum damage the monster can inflict.
            - attack_speed (float): The attack speed of the monster.
            - chance_to_hit (float): The probability of a successful attack.
            - chance_to_heal (float): The probability of the monster healing after an attack.
        """
        super().__init__(name, health, min_damage, max_damage, attack_speed, chance_to_hit)
        self._chance_to_heal = chance_to_heal

    @property
    def chance_to_heal(self):
        """
        Gets the chance for the monster to heal after an attack.

        Returns:
            float: The chance to heal.
        """
        return self._chance_to_heal

    @chance_to_heal.setter
    def chance_to_heal(self, value):
        """
        Sets the chance for the monster to heal after an attack.

        Parameters:
            - value (float): The new chance to heal.
        """
        self._chance_to_heal = value

    def move(self):
        """
        Implements the logic for Monster movement.

        Prints a message indicating that the monster is moving.
        """
        print(f"{self.get_name()} is moving.")

    def heal(self):
        """
        Allows the monster to heal after any attack that causes a loss of hit points.

        The chance to heal is checked after the monster has been attacked and hit points have been lost.
        """
        if self.is_alive() and random.random() < self._chance_to_heal:
            heal_amount = random.randint(15, 30)  # Adjust the healing range as needed
            self.set_health(heal_amount)
            print(f"{self.get_name()} healed itself for {heal_amount} hit points.")

    def attack(self, opponent):
        """
        Attacks the opponent with a chance to heal after the attack.

        Overrides the attack method for the monster's specific attack behavior.

        Parameters:
            - opponent (DungeonCharacter): The opponent to attack.
        """
        if self.can_attack():
            damage = random.randint(self.get_min_damage(), self.get_max_damage())
            opponent.receive_damage(damage)
            print(f"{self.get_name()} attacked {opponent.get_name()} for {damage} damage.")
            self.heal()  # The monster has a chance to heal after any attack
        else:
            print(f"{self.get_name()} missed the attack on {opponent.get_name()}.")
