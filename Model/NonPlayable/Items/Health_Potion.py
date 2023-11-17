import random
from abc import ABC, abstractmethod

from Model.NonPlayable.Items import Item
from Model.Characters.Heroes import Hero


class Health_Potion(Item):

    def __init__(self):
        super().__init__("Health Potion")

    def effect(self, hero: Hero):
        return hero.set_health(random.randint(5, 15))
