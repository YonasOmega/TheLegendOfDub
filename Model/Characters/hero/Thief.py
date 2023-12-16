from Model.Characters.hero.Heroes import Hero
import random


class Thief(Hero):
    """
    Thief class represents a specific type of hero - a Thief, inheriting from Hero.
    """

    def __init__(self, name):
        """
        Initializes a Thief instance with default attributes.


        Parameters:
            - name (str): The name of the thief.
        """
        super().__init__(name, health=75, min_damage=20, max_damage=40, attack_speed=6, chance_to_hit=0.8,
                         chance_to_block=0.4)

    def special_skill(self, opponent):
        """
        Performs the Surprise Attack special skill on the opponent.


        Parameters:
            - opponent (DungeonCharacter): The opponent character to perform the surprise attack on.


        Returns:
            str: A message indicating the result of the special skill.
        """

        # Implement the Surprise Attack special skill
        skill_result = random.random()
        damage = random.randint(self.min_damage, self.max_damage)

        if skill_result < 0.4:  # 40% chance of successful surprise attack
            opponent.receive_damage(damage)
            print(
                f"{self.get_name()} successfully performed a surprise attack on {opponent.get_name()} for {damage} damage and gets an extra turn.")
            print(f"Player health: {self.get_health()}")
            print(f"Monster Health: {opponent.get_health()}")
            Thief.thief_skill(self, opponent)
        elif skill_result < 0.6:  # 20% chance of getting caught
            print(f"{self.get_name()} attempted a surprise attack but got caught. No attack this round.")
        else:  # 40% chance of a normal attack
            opponent.receive_damage(damage)
            print(
                f"{self.get_name()} couldn't get a surprise attack, defaulted to a normal attack on {opponent.get_name()} for {damage} damage.")

    @staticmethod
    def player_choice():
        choice = input("Choose your attack: (1) Normal Attack, (2) Special Attack: ")
        return choice.strip()

    @staticmethod
    def thief_skill(player, monster):
        # Player's turn(s)
        for _ in range(1):
            if monster.get_health() <= 0 or player.get_health() <= 0:
                break
            attack_choice = Thief.player_choice()
            if attack_choice == "1":
                player.attack(monster)
            elif attack_choice == "2":
                player.special_skill(monster)
            else:
                print("Invalid choice, defaulting to normal attack.")
                player.attack(monster)
