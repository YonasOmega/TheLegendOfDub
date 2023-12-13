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

# Initialize Pygame
pygame.init()
pygame.mixer.init()


# Load background music
def load_music():
    # Get the path to the script's directory
    script_directory = Path(__file__).resolve().parent
    music_path = os.path.join(script_directory, "..", "Assets", "Musics", "1 - Adventure Begin.ogg")

    pygame.mixer.music.load(music_path)


load_music()
pygame.mixer.music.play(-1)  # Play the music indefinitely
pygame.mixer.music.set_volume(0.1)


# Function for the introduction screen
def intro_screen():
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
                    how_to_play_screen()  # Call the How to Play screen

        # Fill the screen with a background color
        screen.fill((0, 0, 0))

        # Display the game title
        font = pygame.font.Font(None, 74)
        text = font.render("The Legend of Dub", True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 4))
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
        selected_hero = character_selection_screen()
        # Continue with game setup for a new game
        # ...
        pass


# Function for the "How to Play" screen
def how_to_play_screen():
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
            "OOP pillars, avoid monsters,",
            "and reach the exit for victory.",
            "Use the arrow keys to move.",
            # Add as many lines as needed
        ]
        for i, line in enumerate(instructions):
            text = font.render(line, True, (255, 255, 255))
            screen.blit(text, (20, 50 + 30 * i))

        # Draw Back Button
        pygame.draw.rect(screen, (255, 0, 0) if back_button_area.collidepoint(mouse) else (200, 0, 0), back_button_area)
        text_back = font.render("Back", True, (255, 255, 255))
        screen.blit(text_back, (160, back_button_y_position + 10))

        pygame.display.update()
        clock.tick(15)


# Function to load hero assets based on hero type
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
        pygame.transform.scale(pygame.image.load(os.path.join(hero_images_path, "down", f"down{i}.png")), target_size)
        for i in range(3)
    ]
    assets["left"] = [
        pygame.transform.scale(pygame.image.load(os.path.join(hero_images_path, "left", f"left{i}.png")), target_size)
        for i in range(3)
    ]
    assets["right"] = [
        pygame.transform.scale(pygame.image.load(os.path.join(hero_images_path, "Right", f"Right{i}.png")), target_size)
        for i in range(3)
    ]

    return assets


# Function for the character selection screen
def character_selection_screen():
    selection = True
    font = pygame.font.Font(None, 50)

    # Define button positions and sizes
    button_width = 200
    button_height = 50
    start_x = screen_width // 2 - button_width // 2
    start_y = screen_height // 2 - (3 * button_height + 20) // 2

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
        thief_color = (255, 0, 0) if start_x <= mouse[0] <= start_x + button_width and start_y + button_height + 10 <= \
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


def game_loop(dungeon: Dungeon, player: Hero):
    print("Game loop is happening")
    room = dungeon.get_room(player.position[0], player.position[1])

    if room.exit:
        # Define the set of required pillars
        required_pillars = {"Polymorphism", "Abstraction", "Encapsulation", "Inheritance"}

        # Check if each required pillar is in the player's bag
        has_all_pillars = all(pillar in (str(item) for item in player.bag_object()) for pillar in required_pillars)

        if has_all_pillars:
            return "won"
        else:
            print("There are more pillars to be found")

    if room.pillar:
        print(f"{room.pillar} found!")
        player.put_in_bag(room.pillar)
        room.discard_pillar()

    if room.potion:
        print(f"{room.potion} found!")
        player.put_in_bag(room.potion)
        room.dicard_potioon()

    if room.pit:
        print(f"You fell into a pit. You took {room.pit} damage")
        player.receive_damage(room.pit)

    if room.monster:
        print(f"You have encountered a {room.monster}")
        print(player)
        print(room.monster)
        Combat_Encounter.start_combat(player, room.monster)
        room.monster_defeated()

    elif not player.is_alive():
        return "lost"

    return "continue"


# Set the window size
screen_width = 470
screen_height = 470

# Load images
path_image = pygame.image.load("../Assets/brown.png")
block_background = pygame.image.load("../Assets/white.png")
exit_image = pygame.image.load("../Assets/icons8-close-window-96.png")
entrance_image = pygame.image.load("../Assets/icons8-tick-96.png")
abstraction_image = pygame.image.load("../Assets/icons8-a-48.png")
inheritance_image = pygame.image.load("../Assets/icons8-letter-i-47.png")
encapsulation_image = pygame.image.load("../Assets/icons8-e-48.png")
polymorphism_image = pygame.image.load("../Assets/icons8-p-key-48.png")

# Create the window
screen = pygame.display.set_mode((screen_width, screen_height))

# Fill the window with black
screen.fill((0, 0, 0))

# Update the display
pygame.display.update()

# have a name for our game
pygame.display.set_caption("LegendOfDub")

# Create a DungeonGenerator instance
dungeon = Dungeon(6, 6)
# dungeon_generator = DungeonGenerator(10, 10)  # Set appropriate dimensions


# dungeon_generator.generate()

# Map the characters to their corresponding images
element_images = {
    'X': entrance_image,
    'Y': exit_image,
    #
    'A': abstraction_image,
    'E': encapsulation_image,
    'I': inheritance_image,
    'P': polymorphism_image,
    '1': path_image,
    '0': block_background,
}

# Have a clock so we can so it to 60fps
clock = pygame.time.Clock()

# Intro Screen
intro_screen()

# Character Selection Screen
selected_hero = character_selection_screen()

valid_paths = dungeon.maze.get_Path_Pos()

# start_grid_pos = random.choice(list(valid_paths))  # Grid position
selected_hero.position = dungeon.player_location
start_grid_pos = selected_hero.position

hero_type = selected_hero.__class__.__name__
hero_assets = load_hero_assets(hero_type)

# Convert grid position to pixel position for player start
start_pixel_pos = [start_grid_pos[1] * 47, start_grid_pos[0] * 47]
player_controller = PlayerController(start_pixel_pos, (47, 47), 2, selected_hero, dungeon.maze, hero_assets, selected_hero)

# Save the initial game state
GameState.save_game(selected_hero, player_controller, dungeon.maze)

# Keep the window open until the user closes it
game_status = "continue"
while game_status == "continue":
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Get the current key state
    key_state = pygame.key.get_pressed()

    # Update the player controller
    player_controller.update(key_state)

    # Update the display
    screen.fill((0, 0, 0))

    # Get the path positions from the DungeonGenerator
    path_positions = dungeon.maze.get_Path_Pos()
    pillar_position = dungeon.maze.get_Pill_Pos()

    # Draw the dungeon elements on the screen
    for row_index, row in enumerate(dungeon.maze.get_maze()):
        for col_index, element in enumerate(row):
            position = (row_index, col_index)
            # if position in path_positions:
            #     # Draw a red rectangle for path positions
            #     pygame.draw.rect(screen, (255, 0, 0), (col_index * 47, row_index * 47, 47, 47))
            # elif element in element_images:
            #     # Draw the element image for non-path positions
            #     screen.blit(element_images[element], (col_index * 47, row_index * 47))
            screen.blit(element_images[element], (col_index * 47, row_index * 47))

    player_controller.update_animation()  # Update animation frame
    # Draw the player at the updated position
    player_pos = player_controller.get_position()
    temp_pos = player_controller.get_grid_position()
    selected_hero.position = temp_pos
    print(f"True hero position:  {selected_hero.position}")
    # pygame.draw.rect(screen, (0, 255, 0), (*player_pos, *player_controller.size))
    current_sprites = player_controller.assets[player_controller.current_direction]
    current_sprite = current_sprites[player_controller.current_frame]
    screen.blit(current_sprite, player_pos)

    pygame.display.update()
    game_status = game_loop(dungeon, selected_hero)
    clock.tick(30)  # shouldn't run more than 60 ticks

if game_status == "won":
    print("Congratulations! You have won the game!")
elif game_status == "lost":
    print("You have lost the game. Better luck next time!")

print(dungeon.maze)
