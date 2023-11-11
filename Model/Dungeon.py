import numpy as np
import random

class Dungeon:
    def __init__(self, row: int, col: int):
        self.__Row = row
        self.__Col = col
        self.__Maze = None
        self.__Pillars = ['A', 'E', 'I', 'P']

        # Randomly place entrance and exit ensuring they are different
        self.__EntranceX, self.__EntranceY = self.random_position()
        self.__ExitX, self.__ExitY = self.random_position()
        while self.spaced_entrance_and_exit():
            self.__ExitX, self.__ExitY = self.random_position()

    def random_position(self):
        return random.randint(0, self.__Row - 1), random.randint(0, self.__Col - 1)

    def generate(self):
        # Create a 2D array with all elements initialized to 0
        self.__Maze = [[0 for _ in range(self.__Row)] for _ in range(self.__Col)]
        self.place_entrance_and_Exit()
        self.place_pillars()


    def place_pillars(self):
        placed_pillars = set()  # To track already placed pillars

        for pillar in self.__Pillars:
            x, y = self.random_position()
            # Check if the position is unoccupied and no a path or entrance
            while self.__Maze[x][y] in self.__Pillars or self.__Maze[x][y] == 'X' or self.__Maze[x][y] == 'Y':
                x, y = self.random_position()  # Find a new position

            self.__Maze[x][y] = pillar
            placed_pillars.add((x, y))  # Add the position to the set of placed pillars

    def place_entrance_and_Exit(self):
        self.__Maze[self.__ExitX][self.__ExitY] = 'Y'
        self.__Maze[self.__EntranceX][self.__EntranceY] = 'X'

    def __str__(self):
        # Convert each row of the maze to a string and then join all rows
        return '\n'.join([' '.join(map(str, row)) for row in self.__Maze])

    def spaced_entrance_and_exit(self):
        # Check if the exit is in any of the immediately surrounding positions of the entrance
        return (self.__EntranceX + 1, self.__EntranceY) == (self.__ExitX, self.__ExitY) \
            or (self.__EntranceX - 1, self.__EntranceY) == (self.__ExitX, self.__ExitY) \
            or (self.__EntranceX, self.__EntranceY + 1) == (self.__ExitX, self.__ExitY) \
            or (self.__EntranceX, self.__EntranceY - 1) == (self.__ExitX, self.__ExitY) \
            or (self.__EntranceX + 1, self.__EntranceY + 1) == (self.__ExitX, self.__ExitY) \
            or (self.__EntranceX + 1, self.__EntranceY - 1) == (self.__ExitX, self.__ExitY) \
            or (self.__EntranceX - 1, self.__EntranceY + 1) == (self.__ExitX, self.__ExitY) \
            or (self.__EntranceX - 1, self.__EntranceY - 1) == (self.__ExitX, self.__ExitY)


# Example usage
dungeon = Dungeon(5, 5)
dungeon.generate()
print(dungeon)
