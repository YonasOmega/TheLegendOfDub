from Model.DungeonGenerator import DungeonGenerator


class Dungeon():

    def __init__(self, row: int, col: int):
        self.__dungeon = DungeonGenerator(row, col)
        self.__maze = self.__dungeon.get_maze()


