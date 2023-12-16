from abc import abstractmethod
import random
from Model.Characters.DungeonCharacter import DungeonCharacter

class Hero(DungeonCharacter):
    """
    Hero class represents a heroic character in a dungeon-based game, inheriting from DungeonCharacter.
    """

    def __init__(self, name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_block):
        """
        Initializes a Hero with the specified attributes.

        Parameters:
            - name (str): The name of the hero.
            - health (int): The initial health points of the hero.
            - min_damage (int): The minimum damage the hero can inflict.
            - max_damage (int): The maximum damage the hero can inflict.
            - attack_speed (float): The attack speed of the hero.
            - chance_to_hit (float): The probability of a successful attack.
            - chance_to_block (float): The probability of successfully blocking an attack.
        """
        super().__init__(name, health, min_damage, max_damage, attack_speed, chance_to_hit)
        self.chance_to_block = chance_to_block

    @abstractmethod
    def special_skill(self, opponent):
        """
        Abstract method representing the hero's special skill.

        Parameters:
            - opponent (DungeonCharacter): The opponent to use the special skill on.
        """
        pass

    def block_attack(self):
        """
        Determines if the hero successfully blocks an attack based on chance_to_block.

        Returns:
            bool: True if the attack is blocked, False otherwise.
        """
        return random.random() < self.chance_to_block

    def is_valid_movement(self, new_position, dungeon_generator):
        """
        Checks if the new position is a valid movement within the dungeon boundaries.

        Parameters:
            - new_position (tuple): The new position as a tuple (x, y).
            - dungeon_generator (DungeonGenerator): The dungeon generator providing maze information.

        Returns:
            bool: True if the new position is a valid movement, False otherwise.
        """
        # Check if the new position is within the dungeon boundaries
        dungeon_width = len(dungeon_generator.get_maze()[0])
        dungeon_height = len(dungeon_generator.get_maze())

        if not (0 <= new_position[0] < dungeon_width and 0 <= new_position[1] < dungeon_height):
            return False

        # Check if the new position is a valid path
        valid_paths = dungeon_generator.get_Path_Pos()
        return tuple(new_position) in valid_paths
