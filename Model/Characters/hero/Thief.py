from Model.Characters.hero.Heroes import Hero
import random

class Thief(Hero):
    """
    Thief class represents a specific type of hero - a Thief, inheriting from Hero.
    """

    def __init__(self, name):
        """
        Initializes a Thief instance with default attributes.

        Parameters:
            - name (str): The name of the thief.
        """
        super().__init__(name, health=75, min_damage=20, max_damage=40, attack_speed=6, chance_to_hit=0.8, chance_to_block=0.4)

    def special_skill(self, opponent):
        """
        Performs the Surprise Attack special skill on the opponent.

        Parameters:
            - opponent (DungeonCharacter): The opponent character to perform the surprise attack on.

        Returns:
            str: A message indicating the result of the special skill.
        """
        skill_result = random.random()

        if skill_result < 0.4:  # 40% chance of successful surprise attack
            damage = random.randint(self.get_min_damage(), self.get_max_damage())
            opponent.receive_damage(damage)
            return f"{self.get_name()} successfully performed a surprise attack on {opponent.get_name()} for {damage} damage and gets an extra turn."
        elif skill_result < 0.6:  # 20% chance of getting caught
            return f"{self.get_name()} attempted a surprise attack but got caught. No attack this round."
        else:  # 40% chance of a normal attack
            damage = random.randint(self.get_min_damage(), self.get_max_damage())
            opponent.receive_damage(damage)
            return f"{self.get_name()} performed a normal attack on {opponent.get_name()} for {damage} damage."
