from abc import ABC, abstractmethod
from Character import Character


class PlayableCharacter(ABC):
    def __init__(self, theHero, theLives, theKey, thePillars, theMovementSpeed, theAttackPower, theIsAlive):
        self.hero = Character(theHero)
        self.lives = theLives
        self.key = theKey
        self.pillars = thePillars
        self.movementSpeed = theMovementSpeed
        self.attackPower = theAttackPower
        self.isAlive = theIsAlive
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def movement(self, position):
        pass

    @abstractmethod
    def specialAttack(self):
        pass

    def useItem(self):
        pass
