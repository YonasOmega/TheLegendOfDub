from abc import ABC, abstractmethod
from Character import Character


class NPC(ABC):
    def __init__(self, NPC, movementSpeed, lives, isAlive, attackPower):
        self.NPC = Character(NPC)
        self.movementSpeed = movementSpeed
        self.lives = lives
        self.isAlive = isAlive
        self.attackPower = attackPower

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def randomMovement(self):
        pass

