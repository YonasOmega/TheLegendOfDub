from abc import ABC, abstractmethod
from Character import Character


class NPC(ABC):
    __myNPC = 0
    __myMovementSpeed = 0
    __myLives = 0
    __myIsAlive = 0
    __myAttackPower = 0

    def __init__(self, NPC, movementSpeed, lives, isAlive, attackPower):
        self.__myNPC = Character(NPC)
        self.__myMovementSpeed = movementSpeed
        self.__myLives = lives
        self.__myIsAlive = isAlive
        self.__myAttackPower = attackPower

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def randomMovement(self):
        pass

