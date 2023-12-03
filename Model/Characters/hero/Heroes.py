from abc import abstractmethod
import random
from Model.Characters.DungeonCharacter import DungeonCharacter


class Hero(DungeonCharacter):
    """
    Represents a hero character in the game.

    The Hero class extends the DungeonCharacter with additional attributes and behaviors specific to hero characters,
    such as the ability to block attacks and special skills.

    Attributes:
        chance_to_block (float): The probability that the hero will block an incoming attack.
    """
    def __init__(self, name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_block):
        """
        Initializes a Hero with specified attributes.

        :param name: Name of the hero.
        :param health: Health points of the hero.
        :param min_damage: Minimum damage the hero can inflict.
        :param max_damage: Maximum damage the hero can inflict.
        :param attack_speed: Speed at which the hero can attack.
        :param chance_to_hit: Probability of the hero's attack being successful.
        :param chance_to_block: Probability of the hero blocking an incoming attack.
        """
        super().__init__(name, health, min_damage, max_damage, attack_speed, chance_to_hit)
        self.chance_to_block = chance_to_block

    @abstractmethod
    def special_skill(self, opponent):
        """
        Abstract method defining the hero's special skill.

        This method should be implemented by subclasses to specify the hero's unique special skill used in combat.

        :param opponent: The DungeonCharacter object representing the opponent in combat.
        """
        pass

    def block_attack(self):
        """
        Attempt to block an incoming attack.

        Determines whether an attack is blocked based on the hero's chance_to_block.

        :return: True if the attack is successfully blocked, False otherwise.
        """
        return random.random() < self.chance_to_block

    def receive_damage(self, damage):
        pass
        # if blockattack true, no damage, otherwise get damage
        # apply to monsters as well

    def is_valid_movement(self, new_position, dungeon_generator):
        """
        Check if a proposed movement to a new position is valid within the dungeon.

        Validates if the new position is within the boundaries of the dungeon and not colliding with obstacles.

        :param new_position: Tuple representing the new position (x, y) to move to.
        :param dungeon_generator: Instance of DungeonGenerator representing the current dungeon layout.
        :return: True if the movement is valid, False otherwise.
        """
        # Implement logic to check if the new_position is valid in the dungeon
        # You might want to check if the new_position is within the boundaries of the dungeon
        # and if it doesn't collide with obstacles.

        # Example: Check if the new position is within the dungeon boundaries
        dungeon_width = len(dungeon_generator.get_maze()[0])
        dungeon_height = len(dungeon_generator.get_maze())

        if 0 <= new_position[0] < dungeon_width and 0 <= new_position[1] < dungeon_height:
            return True
        else:
            return False
