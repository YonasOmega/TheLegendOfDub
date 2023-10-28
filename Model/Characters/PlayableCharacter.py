from abc import ABC, abstractmethod
from Character import Character
import pygame


class PlayableCharacter(ABC):

    __myHero = 0
    __myLives = 0
    __myKey = 0
    __myPillars = 0
    __myMovementSpeed = 0
    __myAttackPower = 0
    __myIsAlive = 0

    def __init__(self, theHero, theLives, theKey, thePillars, theMovementSpeed, theAttackPower, theIsAlive):
        self.__myHero = Character(theHero)
        self.__myLives = theLives
        self.__myKey = theKey
        self.__myPillars = thePillars
        self.__myMovementSpeed = theMovementSpeed
        self.__myAttackPower = theAttackPower
        self.__myIsAlive = theIsAlive
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
