import pygame

from Model.DungeonGenerator import DungeonGenerator

pygame.init()

# Set the window size
screen_width = 470
screen_height = 480

# Image
path_image = pygame.image.load("../Assets/brown_field/brown_field_detailed.png")
path_special = pygame.image.load("../Assets/green_field/green_field_deatialed.png")

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
    # 'X': entrance_image,
    # 'Y': exit_image,
    #
    # 'A': pillar_image,
    # 'E': pillar_image,
    # 'I': pillar_image,
    # 'P': pillar_image,
    '1': path_image,
}

#Have a clock so we can so it to 60fps
clock = pygame.time.Clock()

# Keep the window open until the user closes it
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            exit()

    # Draw the dungeon elements on the screen
    for row_index, row in enumerate(dungeon_generator.get_maze()):
        for col_index, element in enumerate(row):
            if element in element_images:
                screen.blit(element_images[element], (col_index * 47, row_index * 48))
            elif element != '0':
                screen.blit(path_special, (col_index * 47, row_index * 48))

    pygame.display.update()
    clock.tick(60)  # shouldn't run more than 60 ticks
