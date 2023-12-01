import random

"""
    0 = nothing
    1 = room/pathway
    X = Entrance
    Y = Exit
    A = Abtraction Pillar
    E = Encapsulation Pillar
    I = Inheritence
    P = Polymorphim
"""

"""
        Column0 | Column1 | Column2
row0    x[0][0] | x[0][1] | x[0][2]
row1    x[1][0] | x[1][1] | x[1][2]
row2    x[2][0] | x[2][1] | x[2][2]
"""


def spaced_entrance_and_exit(tuple1: tuple, tuple2: tuple):
    # Unpack tuples into coordinates
    x1, y1 = tuple1
    x2, y2 = tuple2

    # Check if the exit is not in any of the immediately surrounding positions of the entrance
    # This includes diagonally adjacent positions
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (x1 + dx, y1 + dy) == tuple2:
                return False  # Exit is in one of the surrounding positions

    return True  # Exit is not in any of the surrounding positions


class DungeonGenerator:

    def __init__(self, row: int, col: int):
        self.__Row = row
        self.__Col = col
        self.__Maze = None
        self.__Pillars = ['A', 'E', 'I', 'P']
        self.__PillarPosition = set()
        self.__PathPositions = set()
        self.__ent_exi = set()

        self.generate()

    def random_position(self):
        return random.randint(0, self.__Row - 1), random.randint(0, self.__Col - 1)

    def generate(self):
        self.generate_maze()
        self.generate_entrance_exit()
        self.generate_pillars()
        self.pillar_to_path()



    def __str__(self):
        # Convert each row of the maze to a string and then join all rows
        string = ""
        prefix = ""
        for col in range(0, self.__Col):
            for row in range(0, self.__Row):
                string = string + prefix + self.__Maze[col][row]
                prefix = " "
            prefix = ""
            string += "\n"
        return string

    # Helper Methods
    def generate_entrance_exit(self):
        entrance = self.random_position()
        exit = self.random_position()

        while not spaced_entrance_and_exit(entrance, exit):
            exit = self.random_position()

        self.__Maze[entrance.__getitem__(0)][entrance.__getitem__(1)] = 'X'
        self.__Maze[exit.__getitem__(0)][exit.__getitem__(1)] = 'Y'
        self.__PathPositions.add(entrance)
        self.__PathPositions.add(exit)
        self.__ent_exi.add(entrance)
        self.__ent_exi.add(exit)

        #path portions
        self.point_to_point(entrance, exit)

    def point_to_point(self, tuple1: tuple, tuple2: tuple):
        x1, y1 = tuple1
        x2, y2 = tuple2

        # Create a vertical path
        for i in range(min(x1, x2), max(x1, x2) + 1):
            if self.__Maze[i][y1] == '0':
                self.__Maze[i][y1] = '1'
                self.__PathPositions.add((i, y1))

        # Create a horizontal path
        for j in range(min(y1, y2), max(y1, y2) + 1):
            if self.__Maze[x2][j] == '0':
                self.__Maze[x2][j] = '1'
                self.__PathPositions.add((x2, j))

    def pillar_to_path(self):
        for pillar in self.__PillarPosition:
            manhattan = (1000, 1000)
            a = 0
            b = 0
            for path in self.__PathPositions:
                a = abs(pillar[0] - path[0])
                b = abs(pillar[1] - path[1])
                if (a, b) <= manhattan:
                    manhattan = path
            self.point_to_point(pillar, manhattan)

    def generate_pillars(self):
        for pillar in self.__Pillars:
            pillar_pos = self.random_position()
            while not self.spaced_pillars(pillar_pos):
                pillar_pos = self.random_position()
            self.__Maze[pillar_pos[0]][pillar_pos[1]] = pillar
            self.__PillarPosition.add(pillar_pos)

    def spaced_pillars(self, tuple1: tuple):
        x1, y1 = tuple1

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                # Check for boundary conditions
                if not (0 <= x1 + dx < self.__Col and 0 <= y1 + dy < self.__Row):
                    continue  # Skip checking out of bounds positions

                if self.__Maze[x1 + dx][y1 + dy] != '0':
                    return False  # The position is not suitable for a pillar

        return True  # The position is suitable for a pillar
    def generate_maze(self):
        # Create a 2D array with all elements initialized to 0
        self.__Maze = [['0' for _ in range(self.__Row)] for _ in range(self.__Col)]
        # self.__Maze[0][1] = '1'
        # self.__Maze[0][2] = '1'


    def get_Pill_Pos(self):
        print(f"Pillars : {self.__PillarPosition}")

    def get_Path_Pos(self):
        return self.__PathPositions

    def get_maze(self):
        return self.__Maze



# Example usage
#dun = DungeonGenerator(10, 10)
#print(dun)
# dun.get_Path_Pos()
# dun.get_Pill_Pos()