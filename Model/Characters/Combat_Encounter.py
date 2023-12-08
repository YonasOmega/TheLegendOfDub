from Model.Characters.hero.Warrior import Warrior
from Model.Characters.Monsters.Skeleton import Skeleton
from Model.Characters.DungeonCharacter import DungeonCharacter
from Model.Characters.hero.Heroes import Hero
from Model.Characters.Monsters import Monster


class CombatEncounter:
    def __init__(self, player: Hero, monster: Monster):
        self.player = player
        self.monster = monster

    def calculate_turns(self, attacker_speed, defender_speed):
        return max(1, int(attacker_speed / defender_speed))

    def player_choice(self):
        choice = input("Choose your attack: (1) Normal Attack, (2) Special Attack: ")
        return choice.strip()

    def start_combat(self):
        player_turns = self.calculate_turns(self.player.get_attack_speed(), self.monster.get_attack_speed())
        monster_turns = self.calculate_turns(self.monster.get_attack_speed(), self.player.get_attack_speed())

        while self.player.get_health() > 0 and self.monster.get_health() > 0:
            # Player's turn(s)
            for _ in range(player_turns):
                if self.monster.get_health() <= 0:
                    break
                attack_choice = self.player_choice()
                if attack_choice == "1":
                    self.player.perform_attack(self.monster)
                elif attack_choice == "2":
                    self.player.special_skill(self.monster)
                else:
                    print("Invalid choice, defaulting to normal attack.")
                    self.player.perform_attack(self.monster)

            # Monster's turn(s)
            for _ in range(monster_turns):
                if self.player.get_health() <= 0:
                    break
                self.monster.attack(self.player)

            print(f"Player health: {self.player.get_health()}")
            print(f"Monster Health: {self.monster.get_health()}")

        return "Player" if self.monster.get_health() <= 0 else "Monster"


# Example usage
player = Warrior("warrior")
monster = Skeleton()
combat = CombatEncounter(player, monster)
winner = combat.start_combat()
print(f"The winner is {winner}")
