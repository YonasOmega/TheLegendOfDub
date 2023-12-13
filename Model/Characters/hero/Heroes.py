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

    def receive_damage(self, damage):
        # if self.player_controller.god_mode is not None:  # Check if God Mode is active
        #     if(self.player_controller.god_mode):
        #         print("God Mode active: No damage received.")
        #         return

        # Normal damage processing
        if not self.block_attack():
            self._health -= damage
            #print(f"Received damage: {damage}. Current health: {self._health}")
        else:
            print(f"{self.get_name()} Blocked the attack!")
        # pass
        # if blockattack true, no damage, otherwise get damage
        # apply to monsters as well

    def is_valid_movement(self, new_position, dungeon_generator):
        # Check if the new position is within the dungeon boundaries
        dungeon_width = len(dungeon_generator.get_maze()[0])
        dungeon_height = len(dungeon_generator.get_maze())

        if not (0 <= new_position[0] < dungeon_width and 0 <= new_position[1] < dungeon_height):
            return False

        # Check if the new position is a valid path
        valid_paths = dungeon_generator.get_Path_Pos()
        return tuple(new_position) in valid_paths

    def attack(self, opponent):
        attack_count = self.calculate_attack_count(opponent)

        #for _ in range(attack_count):
        if self.can_attack():
            damage = self.calculate_damage()
            opponent.receive_damage(damage)

            print(f"{self._name} successfully attacked {opponent.get_name()} for {damage} damage.")
        else:
            print(f"{self._name} missed the attack on {opponent.get_name()}.")
        self.__str__()
        opponent.__str__()
