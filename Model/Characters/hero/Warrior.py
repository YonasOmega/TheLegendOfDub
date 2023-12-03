
from Model.Characters.hero.Heroes import Hero
import random

class Warrior(Hero):
    """
    Represents a Warrior character in the game.

    The Warrior is a specialized type of Hero known for strength and resilience. This class inherits from the Hero class
    and implements a unique special skill called 'Crushing Blow', a powerful attack with a chance of inflicting
    significant damage.

    Attributes:
        Inherits all attributes from the Hero class.
    """
    def __init__(self, name):
        """
        Initializes a Warrior with specified attributes.

        :param name: Name of the warrior.
        """
        super().__init__(name, health=125, min_damage=35, max_damage=60, attack_speed=4, chance_to_hit=0.8, chance_to_block=0.2)

    def special_skill(self, opponent):
        """
        Perform the Warrior's special skill: Crushing Blow.

        The Warrior has a chance to execute a powerful attack that can cause a large amount of damage.

        :param opponent: The DungeonCharacter object representing the opponent.
        :return: A string describing the outcome of the Crushing Blow attack.
        """

        # Implement the Crushing Blow special skill
        if random.random() < 0.4:  # 40% chance of success
            damage = random.randint(75, 175)
            opponent.receive_damage(damage)
            return f"{self._name} used Crushing Blow on {opponent.name} for {damage} damage."
        else:
            return f"{self._name} attempted Crushing Blow on {opponent.name} but missed."

    # Optionally, you can override the attack method if the Warrior's attack behavior is different.
    # def attack(self, opponent):
    #     # Custom implementation for Warrior's attack if needed
    #     pass
