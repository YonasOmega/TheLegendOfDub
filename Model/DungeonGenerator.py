import random


"""
Module for generating a dungeon layout for a game.

This module includes a class for generating a dungeon with rooms, pathways, entrance, exit, and pillars representing different concepts (Abstraction, Encapsulation, Inheritance, Polymorphism).

Constants:
    Symbols used to represent different elements in the dungeon:
    0 = nothing
    1 = room/pathway
    X = Entrance
    Y = Exit
    A = Abstraction Pillar
    E = Encapsulation Pillar
    I = Inheritance Pillar
    P = Polymorphism Pillar

        Row0 | ROw1 | Row2
Col0    x[0][0] | x[0][1] | x[0][2]
Col1    x[1][0] | x[1][1] | x[1][2]
Col2    x[2][0] | x[2][1] | x[2][2]
"""


def spaced_entrance_and_exit(tuple1: tuple, tuple2: tuple):
    """
    Check if the entrance and exit points are not immediately adjacent, including diagonally.

    :param tuple1: The coordinates of the entrance.
    :param tuple2: The coordinates of the exit.
    :return: True if entrance and exit are not adjacent, False otherwise.
    """
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
    """
    A class to generate a dungeon layout with various features.

    The dungeon layout includes an entrance, an exit, pillars representing different concepts, and pathways connecting these elements.

    Attributes:
        __Row (int): Number of rows in the dungeon.
        __Col (int): Number of columns in the dungeon.
        __Maze (list): 2D list representing the dungeon layout.
        __Pillars (list): List of pillar symbols.
        __PillarPosition (set): Set of coordinates where pillars are located.
        __PathPositions (set): Set of coordinates forming the pathways.
        __ent_exi (set): Set of coordinates for the entrance and exit.
    """
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
        """
        Generate a random position within the dungeon.

        :return: A tuple representing the random position (row, column).
        """
        return random.randint(0, self.__Col - 1), random.randint(0, self.__Row - 1)

    def generate(self):
        """
        Generate the complete dungeon layout.

        This includes generating the maze structure, entrance and exit, pillars, and the pathways.
        :return: Void
        """
        self.generate_maze()
        self.generate_entrance_exit()
        self.generate_pillars()
        self.pillar_to_path()

    def __str__(self):
        """
        Return a string representation of the dungeon layout.

        :return: A string visualizing the dungeon layout.
        """
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
        """
        Generates and Places the entrance and exit in the Dungeon.

        Randomly selects positions for the entrance and exit, ensuring they are not adjacent.
        It then marks these positions in the maze and adds them to the path and entrance/exit sets.
        Finally, it calls the `point_to_point` method to create a path between the entrance and exit.

        The entrance is marked with 'X' and the exit with 'Y' in the maze representation.

        :return: Void
        """
        entrance = self.random_position()
        exit = self.random_position()

        while not spaced_entrance_and_exit(entrance, exit):
            exit = self.random_position()

        # self.__Maze[entrance.__getitem__(0)][entrance.__getitem__(1)] = 'X'
        self.__Maze[entrance[0]][entrance[1]] = 'X'
        self.__Maze[exit.__getitem__(0)][exit.__getitem__(1)] = 'Y'
        self.__PathPositions.add(entrance)
        self.__PathPositions.add(exit)
        self.__ent_exi.add(entrance)
        self.__ent_exi.add(exit)

        # path portions
        self.point_to_point(entrance, exit)

    def point_to_point(self, tuple1: tuple, tuple2: tuple):
        """
        Create a path in the dungeon from one point to another.

        This method connects two points (tuple1 and tuple2) with a path by setting the corresponding positions in the maze to '1'.
        It first creates a vertical path between the points and then a horizontal path.

        :param tuple1: The coordinates of the starting point (x1, y1).
        :type tuple1: tuple
        :param tuple2: The coordinates of the ending point (x2, y2).
        :type tuple2: tuple

        The path creation process involves two steps:
        1. Vertical Path: Connects the x-coordinates of the two points while keeping the y-coordinate constant.
        2. Horizontal Path: Connects the y-coordinates while keeping the x-coordinate of the second point constant.

        During path creation, if any part of the path overlaps with an existing path (indicated by '1'), that part is skipped to avoid overwriting.
        :return: Void
        """
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
        """
        Connect each pillar to the nearest path in the dungeon.

        This method finds the nearest path position for each pillar using the Manhattan distance and creates a path to it.
        The Manhattan distance is calculated as the sum of the absolute differences of the coordinates.

        For each pillar, the method iterates over all path positions, calculates the distance, and keeps track of the
        nearest path. Then it uses the `point_to_point` method to draw a path between the pillar and this path position.

        :return: Void
        """
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
        """
        Randomly place pillars within the dungeon.

        Each pillar (represented by 'A', 'E', 'I', 'P') is placed in a random position, ensuring it does not
        immediately adjoin any existing elements (other pillars, paths, entrance, or exit).

        The position's suitability is determined by the `spaced_pillars` method. Once a suitable position is found, the
        pillar is marked in the maze and its position is recorded in both `__PillarPosition` and `__PathPositions`.

        :return: Void
        """
        for pillar in self.__Pillars:
            pillar_pos = self.random_position()
            while not self.spaced_pillars(pillar_pos):
                pillar_pos = self.random_position()
            self.__Maze[pillar_pos[0]][pillar_pos[1]] = pillar
            self.__PillarPosition.add(pillar_pos)
            self.__PathPositions.add(pillar_pos)

    def spaced_pillars(self, tuple1: tuple):
        """
        Check if a proposed position is suitable for a pillar.

        The method verifies that the position does not adjoin any existing elements (other pillars, paths, entrance,
        exit) in the maze, including diagonal neighbors. It checks each adjacent position to ensure it's empty
        (represented by '0').

        :param tuple1: Coordinates (x1, y1) of the position being checked.
        :return: True if the position is suitable (i.e., not adjacent to other elements), False otherwise.

        Boundary conditions are accounted for to avoid checking positions outside the maze.

        :return: Void
        """
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
        """
        Generates a row x col maze. Initially with all '0' later to be filled special characters.
        :return: Void
        """
        # Create a 2D array with all elements initialized to 0
        self.__Maze = [['0' for _ in range(self.__Row)] for _ in range(self.__Col)]
        # self.__Maze[0][1] = '1'
        # self.__Maze[0][2] = '1'

    def get_Pill_Pos(self):
        """
        Returns the pillar position
        :return: self.__PillarPosition
        """
        print(f"Pillars : {self.__PillarPosition}")
        return self.__PillarPosition

    def get_Path_Pos(self):
        """
        Returns the Path postion
        :return: self.__PathPositions
        """
        print(f"Paths : {self.__PathPositions}")
        return self.__PathPositions

    def get_maze(self):
        """
        returns the Maze
        :return: self.__Maze
        """
        return self.__Maze


# Example usage
# dun = DungeonGenerator(5, 5)
# print(dun)
# dun.get_Path_Pos()
# dun.get_Pill_Pos()
