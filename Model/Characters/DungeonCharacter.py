from abc import ABC
import random


class DungeonCharacter(ABC):

    def __init__(self, name, health, min_damage, max_damage, attack_speed, chance_to_hit):
        self._name = name
        self._health = health
        self._min_damage = min_damage
        self._max_damage = max_damage
        self._attack_speed = attack_speed
        self._chance_to_hit = chance_to_hit
        self._turns = None

    # @abstractmethod
    # def attack(self, opponent):
    #     pass

    def can_attack(self):  #hit or miss
        return random.random() < self._chance_to_hit

    def calculate_damage(self):
        return random.randint(self._min_damage, self._max_damage)

    def perform_attack(self, opponent):
        attack_count = self.calculate_attack_count(opponent)

        damage_total = 0 # in case of tracking the total damage the character cause in 1 turn
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
        self._turns = self._attack_speed/opponent.get_attack_speed

    def __str__(self):
        return f"Name: {self._name}, Health: {self._health}"
