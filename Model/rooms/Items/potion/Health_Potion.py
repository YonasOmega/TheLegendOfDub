import random

from Model.rooms.Items.Item import Item
from Model.Characters.hero.Heroes import Hero


class Health_Potion(Item):

    def __init__(self):
        super().__init__("Health Potion")

    def effect(self, hero: Hero):
        return hero.set_health(random.randint(5, 15))