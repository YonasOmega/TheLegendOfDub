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
from View.GameState import GameState
from View.Intro import Intro


class End:

    @staticmethod
    def display_full_map(screen, dungeon, element_images):
        screen.fill((0, 0, 0))
        for row_index, row in enumerate(dungeon.maze.get_maze()):
            for col_index, element in enumerate(row):
                screen.blit(element_images[element], (col_index * 47, row_index * 47))
        pygame.display.update()

    @staticmethod
    def show_endgame_message(screen, status):
        # Create a semi-transparent surface
        transparent_surface = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
        transparent_surface.fill((0, 0, 0, 128))  # 128 here is the alpha value for half transparency

        # Render the message text
        font = pygame.font.Font(None, 30)
        message = "Congratulations! You have won the game!" if status == "won" else "You have lost the game. Better luck next time!"
        text = font.render(message, True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

        # Blit the text onto the semi-transparent surface
        transparent_surface.blit(text, text_rect)

        # Blit the semi-transparent surface onto the screen
        screen.blit(transparent_surface, (0, 0))
        pygame.display.update()

    @staticmethod
    def endgame_screen(screen, status, dungeon, clock, element_images):

        # End Music
        pygame.mixer.music.stop()  # Play the music indefinitely
        script_directory = Path(__file__).resolve().parent
        music_path = os.path.join(script_directory, "..", "Assets", "Musics", "15 - Credit Theme.ogg")
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(-1)  # Play the music indefinitely
        pygame.mixer.music.set_volume(0.1)

        End.display_full_map(screen, dungeon, element_images)
        End.show_endgame_message(screen, status)

        new_game_button_area = pygame.Rect(screen.get_width() // 2 - 50, screen.get_height() // 2 + 100, 100, 50)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if new_game_button_area.collidepoint(mouse):
                        # Intro.intro_screen(screen, clock)  # Call the intro screen to start a new game
                        # running = False
                        return True

            pygame.draw.rect(screen, (0, 255, 0), new_game_button_area)
            small_font = pygame.font.Font(None, 35)
            text_new_game = small_font.render("New Game", True, (255, 255, 255))
            screen.blit(text_new_game, (screen.get_width() // 2 - 40, screen.get_height() // 2 + 110))
            pygame.display.update()
            clock.tick(15)
        return False
