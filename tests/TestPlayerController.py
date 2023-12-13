import unittest
from unittest.mock import MagicMock
from Controller.Controller import PlayerController

class TestPlayerController(unittest.TestCase):
    def setUp(self):
        # Create mock objects for dependencies
        self.heroes_model = MagicMock()
        self.dungeon_generator = MagicMock()
        self.assets = {
            "up": [MagicMock()],
            "down": [MagicMock()],
            "left": [MagicMock()],
            "right": [MagicMock()]
        }

        # Create PlayerController instance for testing
        self.player_controller = PlayerController(
            start_pos=[0, 0],
            size=(47, 47),
            speed=2,
            heroes_model=self.heroes_model,
            dungeon_generator=self.dungeon_generator,
            assets=self.assets
        )

    def test_move_updates_position(self):
        # Mock the heroes_model to return True for valid movement
        self.heroes_model.is_valid_movement.return_value = True

        # Call the move method with a specific direction
        self.player_controller.move("UP")

        # Check if the position is updated correctly
        expected_position = [0, -47]  # Assuming 47 is the movement increment
        self.assertEqual(self.player_controller.get_position(), expected_position)

    def test_move_does_not_update_position_on_invalid_movement(self):
        # Mock the heroes_model to return False for invalid movement
        self.heroes_model.is_valid_movement.return_value = False

        # Set an initial position
        initial_position = self.player_controller.get_position()

        # Call the move method with a specific direction
        self.player_controller.move("UP")

        # Check if the position remains unchanged
        self.assertEqual(self.player_controller.get_position(), initial_position)

    def test_update_animation_increments_frame_counter(self):
        initial_frame_counter = self.player_controller.frame_counter

        # Call the update_animation method
        self.player_controller.update_animation()

        # Check if the frame counter is incremented
        self.assertEqual(self.player_controller.frame_counter, initial_frame_counter + 1)

    def tearDown(self):
        # Clean up resources if needed
        pass

if __name__ == '__main__':
    unittest.main()
