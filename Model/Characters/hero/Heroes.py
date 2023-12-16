from abc import abstractmethod
import random
from Model.Characters.DungeonCharacter import DungeonCharacter
from Controller.Controller import PlayerController


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
        self.__chance_to_block = chance_to_block
        self.__bag = []

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
        return random.random() < self.__chance_to_block

    def receive_damage(self, damage):
        """
        Handles receiving damage by the hero, considering the chance to block the attack.

        Parameters:
            - damage (int): The amount of damage to be potentially received.

        Side Effects:
            - If the block is unsuccessful, reduces the hero's health by the damage amount.
            - Prints the outcome: whether the damage was received or blocked.
        """
        # Normal damage processing
        if not self.block_attack():
            self.set_damage(damage)
            print(f"Received damage: {damage}. Current health: {self.get_health()}")
        else:
            print(f"{self.get_name()} Blocked the attack!")

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

        # Check if the new position is a valid path or a pillar position
        valid_paths = dungeon_generator.get_Path_Pos()
        pillar_pos = dungeon_generator.get_Pill_Pos()

        # Check if new position is in valid paths or is a pillar position
        return tuple(new_position) in valid_paths or tuple(new_position) in pillar_pos

    def attack(self, opponent):
        """
        Performs an attack on the opponent, applying damage if the attack is successful.

        Parameters:
            - opponent (DungeonCharacter): The character being attacked.

        Side Effects:
            - If the attack is successful, inflicts damage on the opponent.
            - Prints the outcome of the attack.
        """
        attack_count = self.calculate_attack_count(opponent)
        if self.can_attack():
            damage = self.calculate_damage()
            opponent.receive_damage(damage)

            print(f"{self.get_name()} successfully attacked {opponent.get_name()} for {damage} damage.")
        else:
            print(f"{self.get_name} missed the attack on {opponent.get_name()}.")
        self.__str__()
        opponent.__str__()

    def put_in_bag(self, item):
        """
        Adds an item to the hero's bag.

        Parameters:
            item: The item to be added to the bag.
        """
        self.__bag.append(item)

    @property
    def bag(self):
        """
        Provides a string representation of the contents of the hero's bag.

        Returns:
            str: A string listing the items in the hero's bag, each indexed numerically.
        """
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
        """
        Uses an item from the hero's bag based on its index.

        Parameters:
            item_index (int): The index of the item to use, 1-based.

        Side Effects:
            - If the item is a key item (e.g., a pillar), it cannot be used.
            - Otherwise, the item's effect is applied, and it is removed from the bag.
        """
        item_index = item_index - 1
        if 0 <= item_index < len(self.__bag):
            item = self.__bag[item_index]

            if str(item) in ["Polymorphism", "Abstraction", "Encapsulation", "Inheritance"]:
                print(f"{item} cannot be used. As it's a key")
            else:

                item.effect(self)
                self.remove_item(item_index)
                print(f"Used {item.__str__()}.")

    def remove_item(self, item_index):
        """
        Removes an item from the hero's bag based on its index.

        Parameters:
            item_index (int): The index of the item to remove, 1-based.

        Side Effects:
            - The specified item is removed from the bag if the index is valid.
        """
        if 0 <= item_index < len(self.__bag):
            removed_item = self.__bag.pop(item_index)
            print(f"Removed {removed_item} from bag.")

    def player_use_item(self):
        """
        Prompts the player to select and use an item from the hero's bag.

        Side Effects:
            - Displays the bag's contents and prompts for an index.
            - Uses the selected item if a valid index is provided.
        """
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
        """
        Provides a string representation of the Hero including name, health, and bag contents.

        Returns:
            str: A string that combines the hero's basic info and bag contents.
        """
        return super().__str__() + ", " + self.bag

    def bag_object(self):
        """
        Provides direct access to the hero's bag object (list of items).

        Returns:
            list: The list representing the hero's bag.
        """
        return self.__bag

    @property
    def chance_to_block(self):
        """
        Retrieves the hero's chance to block an attack.

        Returns:
            float: The probability of successfully blocking an attack.
        """
        return self.__chance_to_block


