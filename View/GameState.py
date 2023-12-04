import pickle

class GameState:
    @staticmethod
    def save_game(player, dungeon_generator, file_name='savegame.pkl'):
        game_data = {
            'player_position': player.get_position(),
            'player_stats': {
                'health': player.heroes_model._health,
                'min_damage': player.heroes_model._min_damage,
                'max_damage': player.heroes_model._max_damage,
                'attack_speed': player.heroes_model._attack_speed,
                'chance_to_hit': player.heroes_model._chance_to_hit,
                'chance_to_block': player.heroes_model.chance_to_block
            },
            'maze': dungeon_generator.get_maze()  #SAVE THE DUNGEON INSTEAD
        }

        with open(file_name, 'wb') as f:
            pickle.dump(game_data, f)

    @staticmethod
    def load_game(file_name='savegame.pkl'):
        with open(file_name, 'rb') as f:
            game_data = pickle.load(f)
        return game_data
