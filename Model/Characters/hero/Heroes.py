from abc import abstractmethod
import random
from Model.Characters.DungeonCharacter import DungeonCharacter
from Controller.Controller import PlayerController


class Hero(DungeonCharacter):
    def __init__(self, name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_block):
        super().__init__(name, health, min_damage, max_damage, attack_speed, chance_to_hit)
        self.chance_to_block = chance_to_block
        self.__bag = []

    @abstractmethod
    def special_skill(self, opponent):
        pass

    def block_attack(self):
        return random.random() < self.chance_to_block

    def receive_damage(self, damage):
        # if self.player_controller.god_mode is not None:  # Check if God Mode is active
        #     if(self.player_controller.god_mode):
        #         print("God Mode active: No damage received.")
        #         super().god_mode()
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

        # Check if the new position is a valid path or a pillar position
        valid_paths = dungeon_generator.get_Path_Pos()
        pillar_pos = dungeon_generator.get_Pill_Pos()

        # Check if new position is in valid paths or is a pillar position
        return tuple(new_position) in valid_paths or tuple(new_position) in pillar_pos

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

    def put_in_bag(self, item):
        self.__bag.append(item)

    @property
    def bag(self):
        number = 1
        if len(self.__bag) == 0:
            return "Empty bag"
        output = "Bag: [ "
        for i in self.__bag:
            output += str(number) + ": " + str(i) + ", "  # Ensure each item is converted to string
            number = number + 1
        output += "]"
        return output

    def use_item(self, item_index):
        item_index = item_index - 1
        """ Use an item from the bag """
        if 0 <= item_index < len(self.__bag):
            item = self.__bag[item_index]

            if str(item) in ["Polymorphism", "Abstraction", "Encapsulation", "Inheritance"]:
                print(f"{item} cannot be used. As it's a key")
            else:
                # Apply the item's effect here. This depends on how items are structured.
                # For example: item.apply_effect(self)
                item.effect(self)
                self.remove_item(item_index)
                print(f"Used {item.__str__()}.")

    def remove_item(self, item_index):
        """ Remove an item from the bag """
        if 0 <= item_index < len(self.__bag):
            removed_item = self.__bag.pop(item_index)
            print(f"Removed {removed_item} from bag.")

    def player_use_item(self):
        print(self.bag)  # Display the contents of the bag
        try:
            choice = int(input("Select an item to use (1-based index) or 0 to cancel: "))
            if choice == 0:
                print("No item selected.")
            else:
                self.use_item(choice)
        except ValueError:
            print("Invalid input. Please enter a number.")

    def __str__(self):
        return super().__str__() + " " + self.bag

    def bag_object(self):
        return self.__bag


