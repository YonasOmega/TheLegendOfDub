import pickle
import os

class GameState:
    @staticmethod
    def save_game(player, player_controller, dungeon_generator, file_name='savegame.pkl'):
        game_data = {
            'player_position': player_controller.get_position(),
            'player_stats': {
                'health': player._health,
                'min_damage': player._min_damage,
                'max_damage': player._max_damage,
                'attack_speed': player._attack_speed,
                'chance_to_hit': player._chance_to_hit,
                'chance_to_block': player.chance_to_block
            },
            'maze': dungeon_generator.get_maze()  #SAVE THE DUNGEON INSTEAD
        }
        try:
            with open(file_name, 'wb') as f:
                pickle.dump(game_data, f)
        except Exception as e:
            print(f"Error saving game: {e}")


        with open(file_name, 'wb') as f:
            pickle.dump(game_data, f)

    @staticmethod
    def load_game(file_name='savegame.pkl'):
        if not os.path.exists(file_name):
            print(f"Save file {file_name} does not exist.")
            return None

        try:
            with open(file_name, 'rb') as f:
                game_data = pickle.load(f)

            # Validate game_data structure
            if 'player_position' not in game_data or 'player_stats' not in game_data or 'maze' not in game_data:
                print("Invalid save file structure.")
                return None

            return game_data
        except Exception as e:
            print(f"Error loading game: {e}")
            return None
