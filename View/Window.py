import random

import pygame

from Controller.Controller import PlayerController
from Model.DungeonGenerator import DungeonGenerator
from Model.Characters.hero.Warrior import Warrior
from Model.Characters.hero.Thief import Thief
from Model.Characters.hero.Priestess import Priestess
from View import GameState


pygame.init()
def intro_screen():
    intro = True

    # Define Load Game Button Area
    load_game_button_area = pygame.Rect(150, 320, 100, 50)

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Check for mouse button down event
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 150 + 100 > mouse[0] > 150 and 250 + 50 > mouse[1] > 250:
                    intro = False  # Start the game

                    # Check for clicks on "Load Game"
                    if load_game_button_area.collidepoint(mouse):
                        try:
                            loaded_data = GameState.load_game()
                            # Now use loaded_data to set up the game state
                            intro = False
                        except FileNotFoundError:
                            print("No saved game found.")
                            # Handle the case where no saved game is available

        # Fill the screen with a background color
        screen.fill((0, 0, 0))

        # Display the game title
        font = pygame.font.Font(None, 74)
        text = font.render("The Legend of Dub", True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 4))
        screen.blit(text, text_rect)

        # New Game Button
        mouse = pygame.mouse.get_pos()
        if 150 + 100 > mouse[0] > 150 and 250 + 50 > mouse[1] > 250:
            pygame.draw.rect(screen, (0, 255, 0), [150, 250, 100, 50])
        else:
            pygame.draw.rect(screen, (0, 200, 0), [150, 250, 100, 50])

        small_font = pygame.font.Font(None, 35)
        text_new = small_font.render("New Game", True, (255, 255, 255))
        screen.blit(text_new, [160, 260])

        # Load Game Button (placeholder for future implementation)
        pygame.draw.rect(screen, (200, 200, 0), [150, 320, 100, 50])
        text_load = small_font.render("Load Game", True, (255, 255, 255))
        screen.blit(text_load, [155, 330])

        pygame.display.update()
        clock.tick(15)  # Control the loop run speed
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
                        return Warrior("WarriorName")
                    elif start_y + button_height + 10 <= mouse[1] <= start_y + 2 * button_height + 10:
                        return Thief("ThiefName")
                    elif start_y + 2 * (button_height + 10) <= mouse[1] <= start_y + 3 * button_height + 20:
                        return Priestess("PriestessName")

        # Get the current mouse position
        mouse = pygame.mouse.get_pos()

        # Fill the screen with a background color
        screen.fill((0, 0, 0))

        # Check if the mouse is hovering over a button and change color
        warrior_color = (0, 255, 0) if start_x <= mouse[0] <= start_x + button_width and start_y <= mouse[1] <= start_y + button_height else (0, 200, 0)
        thief_color = (255, 0, 0) if start_x <= mouse[0] <= start_x + button_width and start_y + button_height + 10 <= mouse[1] <= start_y + 2 * button_height + 10 else (200, 0, 0)
        priestess_color = (0, 0, 255) if start_x <= mouse[0] <= start_x + button_width and start_y + 2 * (button_height + 10) <= mouse[1] <= start_y + 3 * button_height + 20 else (0, 0, 200)

        # Draw buttons with the appropriate color based on hover state
        pygame.draw.rect(screen, warrior_color, [start_x, start_y, button_width, button_height])  # Warrior
        pygame.draw.rect(screen, thief_color, [start_x, start_y + button_height + 10, button_width, button_height])  # Thief
        pygame.draw.rect(screen, priestess_color, [start_x, start_y + 2 * (button_height + 10), button_width, button_height])  # Priestess

        # Text for each hero type
        warrior_text = font.render("Warrior", True, (255, 255, 255))
        thief_text = font.render("Thief", True, (255, 255, 255))
        priestess_text = font.render("Priestess", True, (255, 255, 255))

        screen.blit(warrior_text, (start_x + 10, start_y + 10))
        screen.blit(thief_text, (start_x + 10, start_y + button_height + 20))
        screen.blit(priestess_text, (start_x + 10, start_y + 2 * (button_height + 20)))

        pygame.display.update()
        clock.tick(15)  # Control the loop run speed


# Set the window size
screen_width = 470
screen_height = 470


# Image
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

#have a name for our game
pygame.display.set_caption("LegendOfDub")

# Create a DungeonGenerator instance
dungeon_generator = DungeonGenerator(10, 10)  # Set appropriate dimensions


#dungeon_generator.generate()
print(dungeon_generator)

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

#Have a clock so we can so it to 60fps
clock = pygame.time.Clock()

#Intro Screen
intro_screen()

#Character Selection Screen
selected_hero = character_selection_screen()

valid_paths = dungeon_generator.get_Path_Pos()
start_grid_pos = random.choice(list(valid_paths))  # Grid position

# Convert grid position to pixel position for player start
start_pixel_pos = [start_grid_pos[1] * 47, start_grid_pos[0] * 47]
player_controller = PlayerController(start_pixel_pos, (47, 47), 2, selected_hero, dungeon_generator)

# Keep the window open until the user closes it
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Get the current key state
    key_state = pygame.key.get_pressed()

    # Update the player controller
    player_controller.update(key_state)


    #Update the display
    screen.fill((0, 0, 0))

    # Get the path positions from the DungeonGenerator
    path_positions = dungeon_generator.get_Path_Pos()

    # Draw the dungeon elements on the screen
    for row_index, row in enumerate(dungeon_generator.get_maze()):
        for col_index, element in enumerate(row):
            position = (row_index, col_index)
            if position in path_positions:
                # Draw a red rectangle for path positions
                pygame.draw.rect(screen, (255, 0, 0), (col_index * 47, row_index * 47, 47, 47))
            elif element in element_images:
                # Draw the element image for non-path positions
                screen.blit(element_images[element], (col_index * 47, row_index * 47))

    # Draw the player at the updated position
    player_pos = player_controller.get_position()
    pygame.draw.rect(screen, (0, 255, 0), (*player_pos, *player_controller.size))

    pygame.display.update()
    clock.tick(60)  # shouldn't run more than 60 ticks
