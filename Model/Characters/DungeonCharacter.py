from abc import ABC, abstractmethod
import random
from Controller.Controller import PlayerController


class DungeonCharacter(ABC):
    """
       DungeonCharacter class represents a character in a dungeon-based game.
       """

    def __init__(self, name, health, min_damage, max_damage, attack_speed, chance_to_hit):
        """
        Initializes a DungeonCharacter with the specified attributes.


        Parameters:
            - __name (str): The name of the character.
            - __health (int): The initial health points of the character.
            - __min_damage (int): The minimum damage the character can inflict.
            - __max_damage (int): The maximum damage the character can inflict.
            - __attack_speed (float): The attack speed of the character.
            - __chance_to_hit (float): The probability of a successful attack.
            - __turns (int): The turns a character gets when battling
            - __position(tuple): The character's position in the dungeon

        """
        if health < 0 or min_damage < 0 or max_damage < 0 or attack_speed < 0 or chance_to_hit < 0:
            raise ValueError("Attributes must be non-negative.")

        if min_damage > max_damage:
            raise ValueError("Minimum damage cannot be greater than maximum damage.")

        self.__name = name
        self.__health = health
        self.__min_damage = min_damage
        self.__max_damage = max_damage
        self.__attack_speed = attack_speed
        self.__chance_to_hit = chance_to_hit
        self.__turns = None
        self.__position = None

    # @abstractmethod
    # def attack(self, opponent):
    #     pass

    def can_attack(self):  # hit or miss
        """
         Determines if the character can successfully attack based on chance_to_hit.


         Returns:
             bool: True if the attack is successful, False otherwise.
         """
        return random.random() < self.__chance_to_hit

    def calculate_damage(self):
        """
        Calculates a random damage value within the specified range.


        Returns:
            int: The calculated damage value.
        """
        return random.randint(self.__min_damage, self.__max_damage)

    @abstractmethod
    def attack(self, opponent):
        pass

    def calculate_attack_count(self, opponent):
        """
        Calculates the number of attacks based on attack speed ratio.


        Parameters:
            - opponent (DungeonCharacter): The opponent character.


        Returns:
            int: The calculated number of attacks.
              """

        # Calculate the number of attacks based on attack speed ratio
        attack_count = int(self.__attack_speed / opponent.get_attack_speed())
        return max(attack_count, 1)  # Ensure at least one attack per round

    def receive_damage(self, damage):
        """
        Reduces the character's health points based on the received damage.

        Parameters:
            - damage (int): The amount of damage to receive.
        """
        self.__health -= damage

    def is_alive(self):
        """
        Checks if the character is still alive.


        Returns:
            bool: True if the character is alive, False otherwise.
        """
        return self.__health > 0

    def get_name(self):
        """
        Retrieves the name of the character.

        Returns:
            str: The name of the character.
        """
        return self.__name

    def get_health(self):
        """
        Retrieves the current health points of the character.

        Returns:
            int: The current health points.
        """
        return self.__health

    def set_health(self, heal: int):
        """
        Increases the health points of the character by the specified amount.

        Parameters:
            - heal (int): The amount by which to increase the health points.
        """
        self.__health += heal

    def set_damage(self, damage: int):
        self.__health -= damage

    def get_attack_speed(self):
        """
       Retrieves the attack speed of the character.

       Returns:
           float: The attack speed.
       """
        return self.__attack_speed

    def turns(self, opponent):
        """
        Calculates the turns required for one complete attack cycle.

        Parameters:
            - opponent (DungeonCharacter): The opponent character.


        Returns:
            float: The calculated turns.
        """
        self.__turns = self.__attack_speed / opponent.get_attack_speed

    def __str__(self):
        """
        Returns a string representation of the DungeonCharacter.

        Returns:
            str: A string containing the name, health, and position of the character.
        """
        return f"Name: {self.__name}, Health: {self.__health}"

    # Position class. It's meant to either get the position or set a position
    @property
    def position(self):
        """
        Gets or sets the position of the character on the grid.


        Returns:
            tuple or None: The position as a tuple (x, y) or None if not set.
        """

        if self.__position is None:
            # raise ValueError("Position has not been set")
            print("no position")
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the character on the grid.


        Parameters:
           - value (tuple): The position as a tuple (x, y).


        Raises:
            - ValueError: If the position is None.
            - TypeError: If the position is not a tuple.
             - ValueError: If the position tuple does not have two elements.
            - TypeError: If the position coordinates are not integers.
            - ValueError: If the position coordinates are not non-negative.
        """
        if value is None:
            raise ValueError("Position cannot be set to None")
        elif not isinstance(value, tuple):
            raise TypeError("Position must be a tuple")
        elif len(value) != 2:
            raise ValueError("Position must be a tuple of two elements (x, y)")
        elif not all(isinstance(num, int) for num in value):
            raise TypeError("Position coordinates must be integers")
        elif not all(num >= 0 for num in value):
            raise ValueError("Position coordinates must be non-negative")
        else:
            self.__position = value

    def god_mode(self):
        """
        Sets the character's attributes to extremely high values, making it almost invincible.

        This method is typically used for testing or debugging purposes to ensure the character
        can easily win battles.
        """
        self.__health = 999999
        self.__min_damage = 999999
        self.__max_damage = 999999

    def I_want_to_lose(self):
        """
        Sets the character's health to a minimal value, making it almost certain to lose.

        This method is usually for testing scenarios where the character is expected to lose
        battles quickly.
        """
        self.__health = 1

    @property
    def min_damage(self):
        """
        Gets the minimum damage the character can inflict.

        Returns:
             int: The minimum damage.
        """
        return self.__min_damage

    @property
    def max_damage(self):
        """
        Gets the maximum damage the character can inflict.


        Returns:
            int: The maximum damage.
        """
        return self.__max_damage

    @property
    def chance_to_hit(self):
        """
          Retrieves the probability of a successful attack by the character.

          Returns:
             float: The chance of successfully hitting an opponent in an attack.
          """
        return self.__chance_to_hit
