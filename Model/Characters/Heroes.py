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

    def is_valid_movement(self, grid_position, dungeon_generator):
        # Implement logic to check if the new_position is valid in the dungeon
        # You might want to check if the new_position is within the boundaries of the dungeon
        # and if it doesn't collide with obstacles.

        # Example: Check if the new position is within the dungeon boundaries
        maze = dungeon_generator.get_maze()
        dungeon_width = len(maze[0])
        dungeon_height = len(maze)
        print("Validating position:", grid_position, " Cell value:", maze[grid_position[1]][grid_position[0]])
        if 0 <= grid_position[0] < dungeon_width and 0 <= grid_position[1] < dungeon_height:
            return maze[grid_position[1]][grid_position[0]] == '1'

        return False

    def attack(self, opponent): #placeholder
        #implement attack logic
        pass
    def special_skill(self, opponent): #placeholder
        #implement special skill logic
        pass