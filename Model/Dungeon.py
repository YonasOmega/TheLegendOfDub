from Model.DungeonGenerator import DungeonGenerator


class Dungeon():

    def __init__(self):
        self.__dungeon = DungeonGenerator(5, 5)
        self.__maze = self.__dungeon.get_maze()


