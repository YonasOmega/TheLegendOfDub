from Model.DungeonGenerator import DungeonGenerator
from Model.rooms.Room import Room


class Dungeon:

    def __init__(self, row: int, col: int):
        self.__player = None
        self.__dungeon = DungeonGenerator(row, col)
        self.__maze = self.__dungeon.get_maze()
        self.__maze_rooms = [[None for _ in range(row)] for _ in range(col)]
        self.fill_maze()

    def fill_maze(self):
        print("Filling maze:")
        for col in range(len(self.__maze)):
            for row in range(len(self.__maze[col])):
                room = Room((col, row))
                room.generate(self.__maze[col][row])
                self.__maze_rooms[col][row] = room
                print(f"Room at ({col}, {row}): {self.__maze[col][row]}")  # Debug print
                if self.__maze[col][row] == "X":
                    self.__player = (col, row)
                    print(f"Player location set to: {self.player_location}")  # Debug print

    # Rest of the Dungeon class remains the same


    def get_room(self, col, row):
        if 0 <= col < len(self.__maze_rooms) and 0 <= row < len(self.__maze_rooms[col]):
            return self.__maze_rooms[col][row]
        else:
            return None  # or handle this case as you see fit

    @property
    def player_location(self):
        return self.__player

    def get_maze_raw(self):
        return self.__dungeon


# Usage
dungeon = Dungeon(7, 7)

print(dungeon.get_maze_raw())
specific_room = dungeon.get_room(5, 5)  # Get room at col 5, row 5
if specific_room:
    print(specific_room.stat())  # Access Room's stat method

print(f"\nplayer location: {dungeon.player_location}")

