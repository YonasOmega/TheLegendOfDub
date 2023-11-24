from abc import abstractmethod
import random
from Model.Characters.DungeonCharacter import DungeonCharacter


class Hero(DungeonCharacter):
    def __init__(self, name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_block):
        super().__init__(name, health, min_damage, max_damage, attack_speed, chance_to_hit)
        self.chance_to_block = chance_to_block

    @abstractmethod
    def special_skill(self, opponent):
        pass

    def block_attack(self):
        return random.random() < self.chance_to_block
