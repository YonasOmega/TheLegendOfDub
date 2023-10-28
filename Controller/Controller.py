import pygame

pygame.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space")
            elif event.key == pygame.K_UP:
                print("Up")
            elif event.key == pygame.K_DOWN:
                print("Down")
            elif event.key == pygame.K_LEFT:
                print("Left")
            elif event.key == pygame.K_RIGHT:
                print("Right")
            elif event.key == pygame.MOUSEBUTTONDOWN: #mouse button down doesn't work since there isnt a window going on
                print("end")
                exit(0)