from abc import ABC, abstractmethod
import random


class DungeonCharacter(ABC):

    def __init__(self, name, health, min_damage, max_damage, attack_speed, chance_to_hit):
        self._name = name
        self._health = health
        self._min_damage = min_damage
        self._max_damage = max_damage
        self._attack_speed = attack_speed
        self._chance_to_hit = chance_to_hit


    def attack(self, opponent):
        opponent.receive_damage(self, random.randint(self._min_damage, self._max_damage))

    def can_attack(self):  #hit or miss
        return random.random() < self._chance_to_hit

    def calculate_damage(self):
        return random.randint(self._min_damage, self._max_damage)

    def perform_attack(self, opponent):
        if self.can_attack():
            damage = self.calculate_damage()
            opponent.receive_damage(damage)
            return f"{self._name} successfully attacked {opponent.name} for {damage} damage."
        else:
            return f"{self._name} missed the attack on {opponent.name}."

    def receive_damage(self, damage):
        self._health -= damage

    def is_alive(self):
        return self._health > 0

    def get_name(self):
        return self._name

    def get_health(self):
        return self._health

    def get_attack_speed(self):
        return self._attack_speed

    def __str__(self):
        return f"Name: {self._name}, Health: {self._health}"
