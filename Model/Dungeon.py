from Model.DungeonGenerator import DungeonGenerator
from Model.rooms.Room import Room


class Dungeon:
    """
    Dungeon class to manage the dungeon environment including rooms and player location.

    Attributes:
        __player (tuple): The coordinates of the player's location in the dungeon.
        __dungeon (DungeonGenerator): An instance of DungeonGenerator for maze generation.
        __maze (list[list[str]]): The raw maze structure obtained from DungeonGenerator.
        __maze_rooms (list[list[Room]]): 2D list of Room objects representing each cell of the maze.
    """

    def __init__(self, row: int, col: int):
        """
        Initializes a new Dungeon instance.

        :parameter:
            row (int): The number of rows in the dungeon.
            col (int): The number of columns in the dungeon.
        """
        self.__player = None
        self.__dungeon = DungeonGenerator(row, col)
        self.__maze = self.__dungeon.get_maze()
        self.__maze_rooms = [[None for _ in range(row)] for _ in range(col)]
        self.fill_maze()

    def fill_maze(self):
        """
        Populates the maze with Room instances based on the generated maze layout.
        """
        print("Filling maze:")
        for col in range(len(self.__maze)):
            for row in range(len(self.__maze[col])):
                room = Room((col, row))
                room.generate(self.__maze[col][row])
                self.__maze_rooms[col][row] = room
                if self.__maze[col][row] == "X":
                    self.__player = (col, row)

    def get_room(self, col, row):
        """
        Retrieves the Room object at the specified coordinates in the maze.

        Args:
            col (int): The column index in the maze.
            row (int): The row index in the maze.

        Returns:
            Room: The Room object at the specified coordinates, or None if coordinates are invalid.
        """
        if 0 <= col < len(self.__maze_rooms) and 0 <= row < len(self.__maze_rooms[col]):
            return self.__maze_rooms[col][row]
        else:
            return None  # or handle this case as you see fit

    @property
    def player_location(self):
        """
        Gets the current player location in the dungeon.

        Returns:
            tuple: The coordinates of the player's location.
        """
        return self.__player

    @property
    def maze(self):
        """
        Gets the DungeonGenerator instance used for the dungeon.

        Returns:
            DungeonGenerator: The instance of DungeonGenerator used for the maze generation.
        """
        return self.__dungeon


# Usage
# dungeon = Dungeon(7, 7)
#
# print(dungeon.get_maze_raw())
# specific_room = dungeon.get_room(5, 5)  # Get room at col 5, row 5
# if specific_room:
#     print(specific_room.stat())  # Access Room's stat method
#
# print(f"\nplayer location: {dungeon.player_location}")
#dungeon = Dungeon(10, 10)

