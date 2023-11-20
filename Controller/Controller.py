import pygame


class PlayerController:
    # Initialize the player controller
    def __init__(self, start_pos, size, speed):
        self.position = start_pos
        self.size = size
        self.speed = speed

    # Moves the player in given direction
    def move(self, direction):
        if direction == "UP":
            self.position[1] -= self.speed
        elif direction == "DOWN":
            self.position[1] += self.speed
        elif direction == "LEFT":
            self.position[0] -= self.speed
        elif direction == "RIGHT":
            self.position[0] += self.speed

    # Gets the current position of the player
    def get_position(self):
        return self.position

    # Updates the player position based of the key state
    def update(self, key_state):
        if key_state[pygame.K_UP] or key_state[pygame.K_w]:
            self.move("UP")
        elif key_state[pygame.K_DOWN] or key_state[pygame.K_s]:
            self.move("DOWN")
        elif key_state[pygame.K_LEFT] or key_state[pygame.K_a]:
            self.move("LEFT")
        elif key_state[pygame.K_RIGHT] or key_state[pygame.K_d]:
            self.move("RIGHT")

    # Sets the new speed for the player (CAN BE USED FOR BUFFS/DEBUFFS)
    def set_speed(self, new_speed):  # We can use to update speed for boost
        self.speed = new_speed
