import pygame

pygame.init()

# Set up the full screen display
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((800, 600)) #small screen

# Player settings (CAN BE UPDATED BASED ON WHAT YOU'D LIKE)
player_pos = [400, 300]  # Starting position
player_size = (50, 50)   # Size of the player
player_speed = 1         # Speed of movement

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key state detection (CAN USE ARROW KEYS AND WASD KEYS)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_pos[1] -= player_speed
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_pos[1] += player_speed
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_pos[0] -= player_speed
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_pos[0] += player_speed

    # Fill the screen with a color (e.g., black)
    screen.fill((0, 0, 0))

    # Draw the player
    pygame.draw.rect(screen, (255, 255, 255), (*player_pos, *player_size))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()