import pygame

pygame.init()

# Set the window size
screen_width = 640
screen_height = 480

# Create the window
screen = pygame.display.set_mode((screen_width, screen_height))

# Fill the window with black
screen.fill((0, 0, 0))

# Update the display
pygame.display.update()

#have a name for our game
pygame.display.set_caption("LegendOfDub")

#Have a clock so we can so it to 60fps
clock = pygame.time.Clock()

# Keep the window open until the user closes it
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            exit()
    pygame.display.update()
    clock.tick(60)  # shouldn't run more than 60 ticks
    print("click")