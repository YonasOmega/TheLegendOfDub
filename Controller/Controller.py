import pygame


class PlayerController:
    # Initialize the player controller
    def __init__(self, start_pos, size, speed, heroes_model, dungeon_generator):
        self.position = start_pos
        self.size = size
        self.speed = speed
        self.heroes_model = heroes_model #refers to heroes model
        self.dungeon_generator = dungeon_generator
        self.god_mode = False

    # Moves the player in given direction
    def move(self, direction):
        new_position = self.position.copy()
        move_x = 47  # Horizontal movement increment (width of one cell)
        move_y = 47  # Vertical movement increment (height of one cell)
        if direction == "UP":
            new_position[1] -= move_y
        elif direction == "DOWN":
            new_position[1] += move_y
        elif direction == "LEFT":
            new_position[0] -= move_x
        elif direction == "RIGHT":
            new_position[0] += move_x

        # Convert pixel position to grid coordinates
        grid_position = [new_position[1] // 47, new_position[0] // 47]

        # Check with heroes model if the movement is valid
        if self.heroes_model.is_valid_movement(grid_position, self.dungeon_generator):
            self.position = new_position
        print("Trying to move to:", new_position, " Grid position:", grid_position)

    # Gets the current position of the player
    def get_position(self):
        return self.position

    # Updates the player position based of the key state
    def update(self, key_state):
        # First, handle the God Mode toggle
        if key_state[pygame.K_g]:
            if not self.key_held:  # Check if key is not already held down
                self.god_mode = not self.god_mode
                print("God Mode is now", "ON" if self.god_mode else "OFF")
                self.key_held = True  # Mark key as held to prevent continuous toggling
            return  # Skip the rest of the update if toggling God Mode
        elif not any(key_state[key] for key in [pygame.K_UP, pygame.K_w, pygame.K_DOWN, pygame.K_s, pygame.K_LEFT, pygame.K_a, pygame.K_RIGHT, pygame.K_d]):
            self.key_held = False  # Reset key_held if no relevant keys are pressed

        # Then, handle movement
        if key_state[pygame.K_UP] or key_state[pygame.K_w]:
            if not self.key_held:
                self.move("UP")
                self.key_held = True
        elif key_state[pygame.K_DOWN] or key_state[pygame.K_s]:
            if not self.key_held:
                self.move("DOWN")
                self.key_held = True
        elif key_state[pygame.K_LEFT] or key_state[pygame.K_a]:
            if not self.key_held:
                self.move("LEFT")
                self.key_held = True
        elif key_state[pygame.K_RIGHT] or key_state[pygame.K_d]:
            if not self.key_held:
                self.move("RIGHT")
                self.key_held = True

    # Sets the new speed for the player (CAN BE USED FOR BUFFS/DEBUFFS)
    def set_speed(self, new_speed):  # We can use to update speed for boost
        self.speed = new_speed
