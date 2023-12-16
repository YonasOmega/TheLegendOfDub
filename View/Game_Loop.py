import random

import pygame

from Controller.Controller import PlayerController
from Model.DungeonGenerator import DungeonGenerator
from Model.Characters.hero.Warrior import Warrior
from Model.Characters.hero.Thief import Thief
from Model.Characters.hero.Priestess import Priestess
from Model.Characters.hero.Heroes import Hero
from Model.Characters import Combat_Encounter
from Model.rooms.Room import Room
from Model.Dungeon import Dungeon
from View import GameState
import os
from pathlib import Path

from View.End import End
from View.GameState import GameState
from View.Intro import Intro


class Main:

    def __init__(self):
        self.__player_controller = None
        self.__start_grid_position = None
        self.__screen = None
        self.__screen_width = 470
        self.__screen_height = 470
        self.__pygame = pygame

        self.__path_image = self.__pygame.image.load("../Assets/brown.png")
        self.__block_background = self.__pygame.image.load("../Assets/white.png")
        self.__exit_image = self.__pygame.image.load("../Assets/icons8-close-window-96.png")
        self.__entrance_image = self.__pygame.image.load("../Assets/icons8-tick-96.png")
        self.__abstraction_image = self.__pygame.image.load("../Assets/icons8-a-48.png")
        self.__inheritance_image = self.__pygame.image.load("../Assets/icons8-letter-i-47.png")
        self.__encapsulation_image = self.__pygame.image.load("../Assets/icons8-e-48.png")
        self.__polymorphism_image = self.__pygame.image.load("../Assets/icons8-p-key-48.png")

        self.__dungeon = Dungeon(10, 10)
        self.__visibility = [[False for _ in range(10)] for _ in range(10)]

        self.__element_images = {
            'X': self.__entrance_image,
            'Y': self.__exit_image,
            #
            'A': self.__abstraction_image,
            'E': self.__encapsulation_image,
            'I': self.__inheritance_image,
            'P': self.__polymorphism_image,
            '1': self.__path_image,
            '0': self.__block_background,
        }

        self.__clock = pygame.time.Clock()

        self.__selected_hero = None

        self.__valid_paths = self.__dungeon.maze.get_Path_Pos()
        self.main()

    def initialize(self):
        self.__player_controller = None
        self.__start_grid_position = None
        self.__screen = None
        self.__screen_width = 470
        self.__screen_height = 470
        self.__pygame = pygame

        self.__path_image = self.__pygame.image.load("../Assets/brown.png")
        self.__block_background = self.__pygame.image.load("../Assets/white.png")
        self.__exit_image = self.__pygame.image.load("../Assets/icons8-close-window-96.png")
        self.__entrance_image = self.__pygame.image.load("../Assets/icons8-tick-96.png")
        self.__abstraction_image = self.__pygame.image.load("../Assets/icons8-a-48.png")
        self.__inheritance_image = self.__pygame.image.load("../Assets/icons8-letter-i-47.png")
        self.__encapsulation_image = self.__pygame.image.load("../Assets/icons8-e-48.png")
        self.__polymorphism_image = self.__pygame.image.load("../Assets/icons8-p-key-48.png")

        self.__dungeon = Dungeon(10, 10)
        self.__visibility = [[False for _ in range(10)] for _ in range(10)]

        self.__element_images = {
            'X': self.__entrance_image,
            'Y': self.__exit_image,
            #
            'A': self.__abstraction_image,
            'E': self.__encapsulation_image,
            'I': self.__inheritance_image,
            'P': self.__polymorphism_image,
            '1': self.__path_image,
            '0': self.__block_background,
        }

        self.__clock = pygame.time.Clock()

        self.__selected_hero = None

        self.__valid_paths = self.__dungeon.maze.get_Path_Pos()

    def main(self):
        self.initialize()
        self.__pygame.init()
        self.__pygame.mixer.init()

        Intro.load_music()

        self.__screen = self.__pygame.display.set_mode((self.__screen_width, self.__screen_height))
        self.__pygame.display.update()

        # have a name for our game
        self.__pygame.display.set_caption("LegendOfDub")
        Intro.intro_screen(self.__screen, self.__clock)

        self.__selected_hero = Intro.character_selection_screen(self.__screen, self.__clock)
        self.__selected_hero.position = self.__dungeon.player_location

        start_grid_pos = self.__selected_hero.position
        hero_type = self.__selected_hero.__class__.__name__
        hero_assets = Intro.load_hero_assets(hero_type)

        start_pixel_pos = [start_grid_pos[1] * 47, start_grid_pos[0] * 47]
        self.__player_controller = PlayerController(start_pixel_pos, (47, 47), 2, self.__selected_hero,
                                                    self.__dungeon.maze, hero_assets,
                                                    self.__selected_hero)

        # Save the initial game state
        GameState.save_game(self.__selected_hero, self.__player_controller, self.__dungeon.maze)
        self.loop()

    def loop(self):
        game_status = "continue"
        while game_status == "continue":
            for event in self.__pygame.event.get():
                if event.type == self.__pygame.QUIT:
                    self.__pygame.quit()
                    exit()

                if event.type == self.__pygame.KEYDOWN:
                    if event.key == self.__pygame.K_b:
                        self.__selected_hero.player_use_item()

            # Get the current key state
            key_state = self.__pygame.key.get_pressed()

            # Update the player controller
            self.__player_controller.update(key_state)
            self.__player_controller.update_visibility(self.__visibility)

            # update the display
            self.__screen.fill((0, 0, 0))

            # Get the path positions from the DungeonGenerator
            path_positions = self.__dungeon.maze.get_Path_Pos()
            pillar_position = self.__dungeon.maze.get_Pill_Pos()

            for row_index, row in enumerate(self.__dungeon.maze.get_maze()):
                for col_index, element in enumerate(row):
                    if self.__visibility[row_index][col_index]:
                        self.__screen.blit(self.__element_images[element], (col_index * 47, row_index * 47))
                    else:
                        # Draw a black tile or your fog of war representation
                        pygame.draw.rect(self.__screen, (0, 0, 0), (col_index * 47, row_index * 47, 47, 47))

            self.__player_controller.update_animation()  # Update animation frame
            # Draw the player at the updated position
            player_pos = self.__player_controller.get_position()
            temp_pos = self.__player_controller.get_grid_position()
            self.__selected_hero.position = temp_pos
            # print(f"True hero position:  {selected_hero.position}")
            # pygame.draw.rect(screen, (0, 255, 0), (*player_pos, *player_controller.size))
            current_sprites = self.__player_controller.assets[self.__player_controller.current_direction]
            current_sprite = current_sprites[self.__player_controller.current_frame]
            self.__screen.blit(current_sprite, player_pos)

            self.__pygame.display.update()
            game_status = self.game_loop()
            self.__clock.tick(30)  # shouldn't run more than 60 ticks

        if game_status == "won":
            print("Congratulations! You have won the game!")
        elif game_status == "lost":
            print("You have lost the game. Better luck next time!")

        if game_status in ["won", "lost"]:
            if End.endgame_screen(self.__screen, game_status, self.__dungeon, self.__clock, self.__element_images):
                self.main()

    def game_loop(self):
        print("Game loop is happening")
        room = self.__dungeon.get_room(self.__selected_hero.position[0], self.__selected_hero.position[1])

        if room.exit:
            # Define the set of required pillars
            required_pillars = {"Polymorphism", "Abstraction", "Encapsulation", "Inheritance"}

            # Check if each required pillar is in the player's bag
            has_all_pillars = all(
                pillar in (str(item) for item in self.__selected_hero.bag_object()) for pillar in required_pillars)

            if has_all_pillars:
                return "won"
            else:
                print("There are more pillars to be found")

        if room.pillar:
            print(f"{room.pillar} found!")
            self.__selected_hero.put_in_bag(room.pillar)
            room.discard_pillar()

        if room.potion:
            print(f"{room.potion} found!")
            self.__selected_hero.put_in_bag(room.potion)
            room.dicard_potioon()

        if room.pit:
            print(f"You fell into a pit. You took {room.pit} damage")
            self.__selected_hero.receive_damage(room.pit)
            room.discard_pit()

        if room.monster:

            # Combat Music
            pygame.mixer.music.stop()
            script_directory = Path(__file__).resolve().parent
            music_path = os.path.join(script_directory, "..", "Assets", "Musics", "17 - Fight.ogg")
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)

            print(f"You have encountered a {room.monster}")
            print(self.__selected_hero)
            print(room.monster)
            Combat_Encounter.start_combat(self.__selected_hero, room.monster)
            room.monster_defeated()

            # Load back normal music
            Intro.load_music()

        elif not self.__selected_hero.is_alive():
            return "lost"

        return "continue"
