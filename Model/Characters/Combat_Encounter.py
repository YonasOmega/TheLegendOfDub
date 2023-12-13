
def calculate_turns(attacker_speed, defender_speed):
    return max(1, int(attacker_speed / defender_speed))


def player_choice():
    choice = input("Choose your attack: (1) Normal Attack, (2) Special Attack: ")
    return choice.strip()


def start_combat(player, monster):
    player_turns = calculate_turns(player.get_attack_speed(), monster.get_attack_speed())
    monster_turns = calculate_turns(monster.get_attack_speed(), player.get_attack_speed())

    while player.get_health() > 0 and monster.get_health() > 0:
        # Player's turn(s)
        for _ in range(player_turns):
            if monster.get_health() <= 0 or player.get_health() <= 0:
                break
            attack_choice = player_choice()
            if attack_choice == "1":
                player.attack(monster)
            elif attack_choice == "2":
                player.special_skill(monster)
            else:
                print("Invalid choice, defaulting to normal attack.")
                player.attack(monster)

        # Monster's turn(s)
        for _ in range(monster_turns):
            if player.get_health() <= 0 or monster.get_health() <= 0:
                break
            monster.attack(player)

        print(f"Player health: {player.get_health()}")
        print(f"Monster Health: {monster.get_health()}")

    return "Player" if monster.get_health() <= 0 else "Monster"



# # Example usage
# player = Warrior("Thief")
# monster = Skeleton()
# winner = start_combat(player, monster)
# print(f"The winner is {winner}")
