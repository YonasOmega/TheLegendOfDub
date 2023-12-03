from abc import ABC
import random


class DungeonCharacter(ABC):
    """
    Abstract base class representing a character in the dungeon game.

    This class provides common attributes and methods for characters in the game, including heroes and monsters.
    It handles basic functionalities such as attacking, receiving damage, and calculating attack count.

    Attributes:
        _name (str): The name of the character.
        _health (int): The health points of the character.
        _min_damage (int): The minimum damage the character can inflict.
        _max_damage (int): The maximum damage the character can inflict.
        _attack_speed (int): The attack speed of the character.
        _chance_to_hit (float): The probability of the character's attack being successful.
        _turns (int): Number of turns the character gets in one round.
        __position (tuple): The (y, x) position of the character in the dungeon.
    """

    def __init__(self, name, health, min_damage, max_damage, attack_speed, chance_to_hit):
        """
        Initializes a DungeonCharacter with specified attributes.

        :param name: Name of the character.
        :param health: Health points of the character.
        :param min_damage: Minimum damage the character can inflict.
        :param max_damage: Maximum damage the character can inflict.
        :param attack_speed: Speed at which the character can attack.
        :param chance_to_hit: Probability of the character's attack being successful.
        """
        self._name = name
        self._health = health
        self._min_damage = min_damage
        self._max_damage = max_damage
        self._attack_speed = attack_speed
        self._chance_to_hit = chance_to_hit
        self._turns = None
        self.__position = None

    # @abstractmethod
    # def attack(self, opponent):
    #     pass

    def can_attack(self):  # hit or miss
        """
        Determine if the character can successfully execute an attack.

        :return: True if the attack is successful, False otherwise.
        """
        return random.random() < self._chance_to_hit

    def calculate_damage(self):

        return random.randint(self._min_damage, self._max_damage)

    def perform_attack(self, opponent):
        attack_count = self.calculate_attack_count(opponent)

        damage_total = 0  # in case of tracking the total damage the character cause in 1 turn
        attack_messages = []

        for _ in range(attack_count):
            if self.can_attack():
                damage = self.calculate_damage()
                opponent.receive_damage(damage)
                damage_total += damage
                attack_messages.append(f"{self._name} successfully attacked {opponent.get_name()} for {damage} damage.")
            else:
                attack_messages.append(f"{self._name} missed the attack on {opponent.get_name()}.")

        return attack_messages, damage_total

    def calculate_attack_count(self, opponent):
        # Calculate the number of attacks based on attack speed ratio
        attack_count = int(self._attack_speed / opponent.get_attack_speed())
        return max(attack_count, 1)  # Ensure at least one attack per round

    def receive_damage(self, damage):
        self._health -= damage

    def is_alive(self):
        return self._health > 0

    def get_name(self):
        return self._name

    def get_health(self):
        return self._health

    def set_health(self, heal: int):
        self._health += heal

    def get_attack_speed(self):
        return self._attack_speed

    def turns(self, opponent):
        self._turns = self._attack_speed / opponent.get_attack_speed

    def __str__(self):
        return f"Name: {self._name}, Health: {self._health}, Position: {self.__position}"

    # Position class. It's meant to either get the position or set a position
    @property
    def position(self):
        """
        Determine if the character can successfully execute an attack.

        :return: True if the attack is successful, False otherwise.
        """
        if self.__position is None:
            raise ValueError("Position has not been set")
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the character.

        :param value: A tuple of two integers representing the new position (x, y) of the character.
        :raises ValueError: If the value is None, not a tuple, or has invalid coordinates.
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
