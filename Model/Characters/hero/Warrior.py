
from Model.Characters.hero.Heroes import Hero
import random

class Warrior(Hero):
    """
    Warrior class represents a specific type of hero - a Warrior, inheriting from Hero.
    """

    def __init__(self, name):
        """
        Initializes a Warrior instance with default attributes.

        Parameters:
            - name (str): The name of the warrior.
        """
        super().__init__(name, health=125, min_damage=35, max_damage=60, attack_speed=4, chance_to_hit=0.8, chance_to_block=0.2)

    def special_skill(self, opponent):
        """
        Performs the Crushing Blow special skill on the opponent.

        Parameters:
            - opponent (DungeonCharacter): The opponent character to perform the special skill on.

        Returns:
            str: A message indicating the result of the special skill.
        """
        if random.random() < 0.4:  # 40% chance of success
            damage = random.randint(75, 175)
            opponent.receive_damage(damage)
            return f"{self.get_name()} used Crushing Blow on {opponent.get_name()} for {damage} damage."
        else:
            return f"{self.get_name()} attempted Crushing Blow on {opponent.get_name()} but missed."

    # Optionally, you can override the attack method if the Warrior's attack behavior is different.
    # def attack(self, opponent):
    #     # Custom implementation for Warrior's attack if needed
    #     pass
