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


class Intro:
    screen_width = 470
    screen_height = 470

    @staticmethod
    def load_music():
        # Get the path to the script's directory
        script_directory = Path(__file__).resolve().parent
        music_path = os.path.join(script_directory, "..", "Assets", "Musics", "1 - Adventure Begin.ogg")
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(-1)  # Play the music indefinitely
        pygame.mixer.music.set_volume(0.1)

    @staticmethod
    # Function for the introduction screen
    def intro_screen(screen, clock):
        intro = True

        # Define Load Game Button Area
        load_game_button_area = pygame.Rect(150, 320, 100, 50)
        new_game_button_area = pygame.Rect(150, 250, 100, 50)
        how_to_play_button_area = pygame.Rect(150, 390, 100, 50)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()

                    # New Game button clicked
                    if new_game_button_area.collidepoint(mouse):
                        intro = False  # Proceed to character selection
                        loaded_data = None  # Indicate that no game data is loaded

                    # Load Game button clicked
                    elif load_game_button_area.collidepoint(mouse):
                        loaded_data = GameState.load_game()
                        if loaded_data is not None:
                            # Successfully loaded the game data
                            intro = False
                        else:
                            print("No saved game found.")
                            # Optionally, you could display a message on the screen
                    # How to Play button clicked
                    elif how_to_play_button_area.collidepoint(mouse):
                        Intro.how_to_play_screen(screen, clock)  # Call the How to Play screen

            # Fill the screen with a background color
            screen.fill((0, 0, 0))

            # Display the game title
            font = pygame.font.Font(None, 74)
            text = font.render("The Legend of Dub", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Intro.screen_width // 2, Intro.screen_height // 4))
            screen.blit(text, text_rect)

            # Draw New Game, Load Game and How to play button
            mouse = pygame.mouse.get_pos()
            pygame.draw.rect(screen, (0, 255, 0) if new_game_button_area.collidepoint(mouse) else (0, 200, 0),
                             new_game_button_area)
            pygame.draw.rect(screen, (200, 200, 0) if load_game_button_area.collidepoint(mouse) else (200, 200, 0),
                             load_game_button_area)
            pygame.draw.rect(screen, (0, 0, 255) if how_to_play_button_area.collidepoint(mouse) else (0, 0, 200),
                             how_to_play_button_area)

            small_font = pygame.font.Font(None, 35)
            text_new = small_font.render("New Game", True, (255, 255, 255))
            text_load = small_font.render("Load Game", True, (255, 255, 255))
            text_how_to_play = small_font.render("How to Play", True, (255, 255, 255))
            screen.blit(text_new, (160, 260))
            screen.blit(text_load, (155, 330))
            screen.blit(text_how_to_play, (155, 400))

            pygame.display.update()
            clock.tick(15)

        if loaded_data:
            # If loaded_data is not None, it means the Load Game button was clicked and game data was loaded successfully
            # Here you should use the loaded_data to set up the game state
            # For example, update player's position, health, stats, and reconstruct the dungeon
            # ...
            pass
        else:
            # New Game was selected, proceed to character selection
            selected_hero = Intro.character_selection_screen(screen, clock)
            # Continue with game setup for a new game
            # ...
            pass

    @staticmethod
    def how_to_play_screen(screen, clock):
        running = True
        back_button_y_position = 350  # Adjust this value as needed
        back_button_area = pygame.Rect(150, back_button_y_position, 100, 50)

        while running:
            mouse = pygame.mouse.get_pos()  # Move this line outside of the event loop

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button_area.collidepoint(mouse):
                        running = False  # Return to intro screen

            screen.fill((0, 0, 0))

            # Display the How to Play text
            font = pygame.font.Font(None, 35)
            instructions = [
                "Welcome to our Game!",
                " ",
                "In order to win you must collect ",
                "OOP pillars, defeat monsters,",
                "and reach the exit for victory.",
                "Use the arrow keys to move.",
                "press g for god-mode, i for lose mode.",
                "press b to use items."
                # Add as many lines as needed
            ]
            for i, line in enumerate(instructions):
                text = font.render(line, True, (255, 255, 255))
                screen.blit(text, (20, 50 + 30 * i))

            # Draw Back Button
            pygame.draw.rect(screen, (255, 0, 0) if back_button_area.collidepoint(mouse) else (200, 0, 0),
                             back_button_area)
            text_back = font.render("Back", True, (255, 255, 255))
            screen.blit(text_back, (160, back_button_y_position + 10))

            pygame.display.update()
            clock.tick(15)

    @staticmethod
    def load_hero_assets(hero_type):
        assets = {}
        target_size = (47, 47)

        # Get the path to the script's directory
        script_directory = Path(__file__).resolve().parent

        if hero_type == "Warrior":
            hero_images_path = os.path.join(script_directory, "..", "Assets", "Character", "Warrior")
        elif hero_type == "Thief":
            hero_images_path = os.path.join(script_directory, "..", "Assets", "Character", "thief")
        elif hero_type == "Priestess":
            hero_images_path = os.path.join(script_directory, "..", "Assets", "Character", "priestess")
        else:
            # Handle unknown hero types here
            raise ValueError(f"Unknown hero type: {hero_type}")

        assets["up"] = [
            pygame.transform.scale(pygame.image.load(os.path.join(hero_images_path, "up", f"up{i}.png")), target_size)
            for i in range(3)
        ]
        assets["down"] = [
            pygame.transform.scale(pygame.image.load(os.path.join(hero_images_path, "down", f"down{i}.png")),
                                   target_size)
            for i in range(3)
        ]
        assets["left"] = [
            pygame.transform.scale(pygame.image.load(os.path.join(hero_images_path, "left", f"left{i}.png")),
                                   target_size)
            for i in range(3)
        ]
        assets["right"] = [
            pygame.transform.scale(pygame.image.load(os.path.join(hero_images_path, "Right", f"Right{i}.png")),
                                   target_size)
            for i in range(3)
        ]

        return assets

    @staticmethod
    def character_selection_screen(screen, clock):
        selection = True
        font = pygame.font.Font(None, 50)

        # Define button positions and sizes
        button_width = 200
        button_height = 50
        start_x = Intro.screen_width // 2 - button_width // 2
        start_y = Intro.screen_height // 2 - (3 * button_height + 20) // 2

        while selection:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    # Check for clicks on each hero's button
                    if start_x <= mouse[0] <= start_x + button_width:
                        if start_y <= mouse[1] <= start_y + button_height:
                            return Warrior("Warrior")
                        elif start_y + button_height + 10 <= mouse[1] <= start_y + 2 * button_height + 10:
                            return Thief("Thief")
                        elif start_y + 2 * (button_height + 10) <= mouse[1] <= start_y + 3 * button_height + 20:
                            return Priestess("Priestess")

            # Get the current mouse position
            mouse = pygame.mouse.get_pos()

            # Fill the screen with a background color
            screen.fill((0, 0, 0))

            # Check if the mouse is hovering over a button and change color
            warrior_color = (0, 255, 0) if start_x <= mouse[0] <= start_x + button_width and start_y <= mouse[
                1] <= start_y + button_height else (0, 200, 0)
            thief_color = (255, 0, 0) if start_x <= mouse[
                0] <= start_x + button_width and start_y + button_height + 10 <= \
                                         mouse[1] <= start_y + 2 * button_height + 10 else (200, 0, 0)
            priestess_color = (0, 0, 255) if start_x <= mouse[0] <= start_x + button_width and start_y + 2 * (
                    button_height + 10) <= mouse[1] <= start_y + 3 * button_height + 20 else (0, 0, 200)

            # Draw buttons with the appropriate color based on hover state
            pygame.draw.rect(screen, warrior_color, [start_x, start_y, button_width, button_height])  # Warrior
            pygame.draw.rect(screen, thief_color,
                             [start_x, start_y + button_height + 10, button_width, button_height])  # Thief
            pygame.draw.rect(screen, priestess_color,
                             [start_x, start_y + 2 * (button_height + 10), button_width, button_height])  # Priestess

            # Text for each hero type
            warrior_text = font.render("Warrior", True, (255, 255, 255))
            thief_text = font.render("Thief", True, (255, 255, 255))
            priestess_text = font.render("Priestess", True, (255, 255, 255))

            screen.blit(warrior_text, (start_x + 10, start_y + 10))
            screen.blit(thief_text, (start_x + 10, start_y + button_height + 20))
            screen.blit(priestess_text, (start_x + 10, start_y + 2 * (button_height + 20)))

            pygame.display.update()
            clock.tick(15)  # Control the loop run speed
