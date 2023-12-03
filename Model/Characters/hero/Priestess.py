import random

from Model.Characters.hero.Heroes import Hero


class Priestess(Hero):
    """
    Represents a Priestess character in the game.

    The Priestess is a specialized type of Hero with unique attributes and a special skill for healing.
    Inherits from the Hero class and implements the special skill for healing allies or self.

    Attributes:
        Inherits all attributes from the Hero class.
    """
    def __init__(self, name):
        """
        Initializes a Priestess with specified attributes.

        :param name: Name of the priestess.
        """
        super().__init__(name, health=75, min_damage=25, max_damage=45, attack_speed=5, chance_to_hit=0.7, chance_to_block=0.3)

    def special_skill(self, target):
        """
        Perform the Priestess's special healing skill.

        Heals the target by a random amount between 15 and 30 hit points.

        :param target: The DungeonCharacter object representing the healing target.
        :return: A string describing the healing action performed.
        """
        # Implement the heal special skill
        heal_amount = random.randint(15, 30)  # Adjust the healing range as needed
        target.receive_healing(heal_amount)
        return f"{self._name} used heal on {target.name}, healing {heal_amount} hit points."

    def receive_healing(self, amount):
        """
        Receive healing.

        Increases the Priestess's health by the specified amount.

        :param amount: The amount of health to be added.
        """
        self._health += amount

    # def attack(self, opponent):

# Example usage:
# priestess = Priestess("PriestessName")

