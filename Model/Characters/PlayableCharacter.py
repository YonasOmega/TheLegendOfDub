from abc import ABC, abstractmethod
from Character import Character
import pygame


class PlayableCharacter(ABC, Character):

    __myLives = 0
    __myKey = 0
    __myPillars = 0
    __myMovementSpeed = 0
    __myAttackPower = 0
    __myIsAlive = 0

    def __init__(self, the_Hero: str, the_Lives: int, the_Key: bool, the_Pillars: bool, the_Movement_Speed: int, the_Attack_Power: int, the_Is_Alive: bool):
        super().__init__(the_Hero)
        self.__myLives = the_Lives
        self.__myKey = the_Key
        self.__myPillars = the_Pillars
        self.__myMovementSpeed = the_Movement_Speed
        self.__myAttackPower = the_Attack_Power
        self.__myIsAlive = the_Is_Alive
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
