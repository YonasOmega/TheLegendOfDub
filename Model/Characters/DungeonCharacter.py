from abc import ABC, abstractmethod
import random
from Controller.Controller import PlayerController


class DungeonCharacter(ABC):

    def __init__(self, name, health, min_damage, max_damage, attack_speed, chance_to_hit):
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
        return random.random() < self.__chance_to_hit

    def calculate_damage(self):
        return random.randint(self.__min_damage, self.__max_damage)

    @abstractmethod
    def attack(self, opponent):
        pass

    def calculate_attack_count(self, opponent):
        # Calculate the number of attacks based on attack speed ratio
        attack_count = int(self.__attack_speed / opponent.get_attack_speed())
        return max(attack_count, 1)  # Ensure at least one attack per round

    def receive_damage(self, damage):
        self.__health -= damage

    def is_alive(self):
        return self.__health > 0

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def set_health(self, heal: int):
        self.__health += heal

    def get_attack_speed(self):
        return self.__attack_speed

    def turns(self, opponent):
        self.__turns = self.__attack_speed / opponent.get_attack_speed

    def __str__(self):
        return f"Name: {self.__name}, Health: {self.__health}"

    # Position class. It's meant to either get the position or set a position
    @property
    def position(self):
        if self.__position is None:
            # raise ValueError("Position has not been set")
            print("no position")
        return self.__position

    @position.setter
    def position(self, value):
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
        self.__health = 999999
        self.__min_damage = 999999
        self.__max_damage = 999999

    def I_want_to_lose(self):
        self.__health = 1

    @property
    def min_damage(self):
        return self.__min_damage

    @property
    def max_damage(self):
        return self.__max_damage

    @property
    def chance_to_hit(self):
        return self.__chance_to_hit
