from Model.DungeonGenerator import DungeonGenerator
from Model.rooms.Room import Room


class Dungeon:

    def __init__(self, row: int, col: int):
        self.__dungeon = DungeonGenerator(row, col)
        self.__maze = self.__dungeon.get_maze()
        self.__maze_rooms = [[None for _ in range(row)] for _ in range(col)]
        self.fill_maze()
        print("stop")

    def fill_maze(self):
        for col in range(len(self.__maze)):
            for row in range(len(self.__maze[col])):
                room = Room()
                room.generate(self.__maze[col][row], (col, row))
                self.__maze_rooms[col][row] = room

    def get_room(self, col, row):
        if 0 <= col < len(self.__maze_rooms) and 0 <= row < len(self.__maze_rooms[col]):
            return self.__maze_rooms[col][row]
        else:
            return None  # or handle this case as you see fit


# Usage
dungeon = Dungeon(11, 12)
specific_room = dungeon.get_room(5, 5)  # Get room at col 5, row 5
if specific_room:
    print(specific_room.stat())  # Access Room's stat method



