from abc import ABC

from Model.Characters.DungeonCharacter import DungeonCharacter
import random


class Monster(DungeonCharacter, ABC):
    """
    Abstract base class representing a monster in the game.

    Inherits from DungeonCharacter and adds specific attributes and behaviors for monsters, including a chance to heal.

    Attributes:
        _chance_to_heal (float): Probability of the monster healing itself after an attack.
    """
    def __init__(self, name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal):
        """
        Initialize a Monster with specified attributes.

        :param name: Name of the monster.
        :param health: Health points of the monster.
        :param min_damage: Minimum damage the monster can inflict.
        :param max_damage: Maximum damage the monster can inflict.
        :param attack_speed: Speed at which the monster can attack.
        :param chance_to_hit: Probability of the monster's attack being successful.
        :param chance_to_heal: Probability of the monster healing itself after an attack.
        """
        super().__init__(name, health, min_damage, max_damage, attack_speed, chance_to_hit)
        self._chance_to_heal = chance_to_heal

    @property
    def chance_to_heal(self):
        """
        Get the chance of the monster to heal itself.

        :return: The chance of the monster to heal itself.
        """
        return self._chance_to_heal

    @chance_to_heal.setter
    def chance_to_heal(self, value):
        """
        Set the chance of the monster to heal itself.

        :param value: A float representing the new chance to heal.
        """
        self._chance_to_heal = value

    def heal(self):
        """
        Attempt to heal the monster.

        The monster has a chance, determined by _chance_to_heal, to heal itself after an attack.
        The amount of healing is a random number between 15 and 30 hit points.
        Healing only occurs if the monster is still alive and the random chance is successful.
        """
        # A Monster has a chance to heal after any attack that causes a loss of hit points
        # The chance to heal is checked after the Monster has been attacked and hit points have been lost
        if self.is_alive() and random.random() < self._chance_to_heal:
            heal_amount = random.randint(15, 30)  # Adjust the healing range as needed
            self._health += heal_amount
            print(f"{self._name} healed itself for {heal_amount} hit points.")
