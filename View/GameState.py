import pickle
import os
from Model.Characters.hero.Heroes import Hero

class GameState:
    """
    Saves the game state to a file.

    Parameters:
    - player: The player object.
    - player_controller: The player controller object.
    - dungeon_generator: The dungeon generator object.
    - file_name: The name of the file to save the game state (default is 'savegame.pkl').
    """
    @staticmethod
    def save_game(player: Hero, player_controller, dungeon_generator, file_name='savegame.pkl'):
        game_data = {
            'player_position': player_controller.get_position(),
            'player_stats': {
                'health': player.get_health(),
                'min_damage': player.min_damage,
                'max_damage': player.max_damage,
                'attack_speed': player.get_attack_speed(),
                'chance_to_hit': player.chance_to_hit,
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
        """
        Loads the game state from a file.

        Parameters:
        - file_name: The name of the file to load the game state from (default is 'savegame.pkl').

        Returns:
        - The loaded game data if successful, otherwise None.
        """
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
