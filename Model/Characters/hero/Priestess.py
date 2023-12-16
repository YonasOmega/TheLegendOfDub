import random

from Model.Characters.hero.Heroes import Hero


class Priestess(Hero):
    """
    Priestess class represents a specific type of hero - a Priestess, inheriting from Hero.
    """

    def __init__(self, name):
        """
        Initializes a Priestess instance with default attributes.


        Parameters:
            - name (str): The name of the priestess.
        """
        super().__init__(name, health=75, min_damage=25, max_damage=45, attack_speed=5, chance_to_hit=0.7, chance_to_block=0.3)

    def special_skill(self, target):
        """
        Performs the heal special skill on the target.


        Parameters:
            - target (DungeonCharacter): The target character to heal.


        Returns:
            str: A message indicating the result of the heal special skill.
        """
        # Implement the heal special skill
        heal_amount = random.randint(15, 30)  # Adjust the healing range as needed
        self.receive_healing(heal_amount)
        print(f"{self.get_name()} healed back {heal_amount} hit points.")

    def receive_healing(self, amount):
        """
        Receives healing by increasing the health points.


        Parameters:
            - amount (int): The amount of healing to receive.
        """
        self.set_health(amount)
