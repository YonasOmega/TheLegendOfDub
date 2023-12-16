from abc import ABC
import random


class DungeonCharacter(ABC):
    """
    DungeonCharacter class represents a character in a dungeon-based game.
    """

    def __init__(self, name, health, min_damage, max_damage, attack_speed, chance_to_hit):
        """
        Initializes a DungeonCharacter with the specified attributes.

        Parameters:
            - name (str): The name of the character.
            - health (int): The initial health points of the character.
            - min_damage (int): The minimum damage the character can inflict.
            - max_damage (int): The maximum damage the character can inflict.
            - attack_speed (float): The attack speed of the character.
            - chance_to_hit (float): The probability of a successful attack.
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

    def perform_attack(self, opponent):
        """
        Performs one or more attacks on the opponent.

        Parameters:
            - opponent (DungeonCharacter): The opponent to attack.

        Returns:
            tuple: A tuple containing a list of attack messages and the total damage inflicted.
        """
        attack_count = self.calculate_attack_count(opponent)

        damage_total = 0  # in case of tracking the total damage the character cause in 1 turn
        attack_messages = []

        for _ in range(attack_count):
            if self.can_attack():
                damage = self.calculate_damage()
                opponent.receive_damage(damage)
                damage_total += damage
                attack_messages.append(f"{self.__name} successfully attacked {opponent.get_name()} for {damage} damage.")
            else:
                attack_messages.append(f"{self.__name} missed the attack on {opponent.get_name()}.")

        return attack_messages, damage_total

    def calculate_attack_count(self, opponent):
        """
       Calculates the number of attacks based on attack speed ratio.

       Parameters:
           - opponent (DungeonCharacter): The opponent character.

       Returns:
           int: The calculated number of attacks.
       """
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
        if heal < 0:
            raise ValueError("Healing amount must be non-negative.")
        self.__health += heal

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
        self._turns = self.__attack_speed / opponent.get_attack_speed

    def __str__(self):
        """
        Returns a string representation of the DungeonCharacter.

        Returns:
            str: A string containing the name, health, and position of the character.
        """
        return f"Name: {self.__name}, Health: {self.__health}, Position: {self.__position}"

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

    def get_x_position(self):
        """
        Retrieves the x-coordinate of the character's position.

        Returns:
            int or None: The x-coordinate or None if the position is not set.
        """
        if self.__position is None:
            # handle the case where position is not set
            return None
        return self.__position[0]

    def get_y_position(self):
        """
        Retrieves the y-coordinate of the character's position.

        Returns:
            int or None: The y-coordinate or None if the position is not set.
        """
        if self.__position is None:
            # handle the case where position is not set
            return None
        return self.__position[1]

    def get_min_damage(self):
        """
        Gets the minimum damage the character can inflict.

        Returns:
            int: The minimum damage.
        """
        return self.__min_damage

    def get_max_damage(self):
        """
        Gets the maximum damage the character can inflict.

        Returns:
            int: The maximum damage.
        """
        return self.__max_damage
