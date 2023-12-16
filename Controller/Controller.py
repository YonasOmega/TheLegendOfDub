import pygame


class PlayerController:
    """
    Manages the player's movement, animation, and interactions within the game.

    Attributes:
        position (list): The current position of the player in (x, y) coordinates.
        size (tuple): The size of the player.
        speed (int): The movement speed of the player.
        heroes_model (Hero): Reference to the heroes model.
        dungeon_generator (DungeonGenerator): Reference to the dungeon generator.
        god_mode (bool): Indicates whether the god mode is activated.
        assets (dict): Assets for player's animation in different directions.
        current_direction (str): The current direction of the player.
        current_frame (int): The current animation frame.
        frame_counter (int): Counter for controlling animation speed.
        __player (Player): Reference to the player object.
    """
    def __init__(self, start_pos, size, speed, heroes_model, dungeon_generator, assets, player):
        """
        Initializes the PlayerController.

        Parameters:
        - start_pos: Starting position of the player (x, y).
        - size: Size of the player.
        - speed: Speed of the player's movement.
        - heroes_model: Reference to the heroes model.
        - dungeon_generator: Reference to the dungeon generator.
        - assets: Dictionary containing player animation assets for different directions.
        """
        self.position = start_pos
        self.size = size
        self.speed = speed
        self.heroes_model = heroes_model  # refers to heroes model
        self.dungeon_generator = dungeon_generator
        self.god_mode = False
        self.assets = assets
        self.current_direction = "down"
        self.current_frame = 0
        self.frame_counter = 0
        self.__player = player

    def move(self, direction):
        """
        Moves the player in the specified direction.

        Parameters:
        - direction: The direction in which the player should move ('UP', 'DOWN', 'LEFT', 'RIGHT').
        """
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
        self.current_direction = direction.lower()  # Update current direction

        # Convert pixel position to grid coordinates
        grid_position = [new_position[1] // 47, new_position[0] // 47]

        # Check with heroes model if the movement is valid
        if self.heroes_model.is_valid_movement(grid_position, self.dungeon_generator):
            self.position = new_position
        print("Trying to move to:", new_position, " Grid position:", grid_position)

    # Gets the current position of the player
    def get_position(self):
        """
        Returns the current position of where the controller is
        :return:
        """
        return self.position

    def get_grid_position(self):
        """
        Returns the current grid position of where the controller is
        :return:
        """
        grid_position = (self.position[1] // 47, self.position[0] // 47)
        return grid_position

    # Updates the player position based of the key state
    def update(self, key_state):
        """
        Updates the player's position based on the current key state.

        Parameters:
            key_state (dict): Dictionary representing the state of keys.
        """
        # First, handle the God Mode toggle
        if key_state[pygame.K_g]:
            if not self.key_held:  # Check if key is not already held down
                #self.god_mode = not self.god_mode
                self.__player.god_mode()
                print("God Mode is now", "ON")
                self.key_held = True  # Mark key as held to prevent continuous toggling
            return  # Skip the rest of the update if toggling God Mode
        elif key_state[pygame.K_i]:
            if not self.key_held:  # Check if key is not already held down
                #self.god_mode = not self.god_mode
                self.__player.I_want_to_lose()
                print("lose Mode is now", "ON")
                self.key_held = True  # Mark key as held to prevent continuous toggling
        elif not any(key_state[key] for key in
                     [pygame.K_UP, pygame.K_w, pygame.K_DOWN, pygame.K_s, pygame.K_LEFT, pygame.K_a, pygame.K_RIGHT,
                      pygame.K_d]):
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

    def update_animation(self):
        """
        Updates the player's animation frame for smooth movement.
        """
        self.frame_counter += 1
        if self.frame_counter >= 60:  # FRAME_DELAY controls the speed of the animation
            self.frame_counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.assets[self.current_direction])

    def set_speed(self, new_speed):  # We can use to update speed for boost
        """
        Sets the new speed for the player. (optional)

        Parameters:
        - new_speed: The new speed value.
        """        """
            Sets the new speed for the player.

            Parameters:
            - new_speed: The new speed value.
            """
        self.speed = new_speed

    @property
    def god_mode(self):
        """
        Getter for god mode attribute.
        :return: God mode
        """
        return self.god_mode

    @god_mode.setter
    def god_mode(self, value):
        """
        Sets the value for the god_mode attribute
        :param value: the value god is going to be
        """
        self._god_mode = value

    def update_visibility(self, visibility):
        """
        Updates the visibility grid based on the player's current position.

        Parameters:
            visibility (list of lists): A 2D list representing the visibility grid.
        """
        x, y = self.__player.position
        visibility[x][y] = True
        # Optionally, reveal adjacent tiles as well
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(visibility) and 0 <= ny < len(visibility[0]):
                    visibility[nx][ny] = True
