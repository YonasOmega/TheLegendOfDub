import numpy as np
import random

class Dungeon:
    def __init__(self, row: int, col: int):
        self.__Row = row
        self.__Col = col
        self.__Maze = None
        self.__Pillars = ['A', 'E', 'I', 'P']
        self.__PillarPosition = set()
        self.__PathPositions = set()

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
        self.entrance_to_exit()
        self.pillars_to_path()

    def entrance_to_exit(self):
        self.entrance_to_exit_y()
        self.entrance_to_exit_x()

    def place_pillars(self):
        for pillar in self.__Pillars:
            x, y = self.random_position()
            # Check if the position is unoccupied, not adjacent to critical points, and within bounds
            while not self.valid_pillar_position(x, y):
                x, y = self.random_position()

            self.__Maze[x][y] = pillar
            self.__PillarPosition.add((x, y))  # Add the position to the set of placed pillars


    def __str__(self):
        # First line with row and column count
        first_line = f"{self.__Row} {self.__Col}"

        # Create each row of the maze
        rows = [" ".join(str(cell) for cell in self.__Maze[i]) for i in range(self.__Row)]

        # Combine first line and rows
        return first_line + "\n" + "\n".join(rows)

    # Helper Methods
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

    def valid_pillar_position(self, x, y):
        if self.__Maze[x][y] in self.__Pillars or self.__Maze[x][y] in ['X', 'Y']:
            return False  # Occupied by another pillar or critical point

        # Check surrounding cells
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.__Row and 0 <= ny < self.__Col:
                    if self.__Maze[nx][ny] != 0:
                        return False

        return True

    def place_entrance_and_Exit(self):
        self.__Maze[self.__ExitX][self.__ExitY] = 'Y'
        self.__Maze[self.__EntranceX][self.__EntranceY] = 'X'
        self.__PathPositions.add((self.__ExitX, self.__ExitY))
        self.__PathPositions.add((self.__EntranceX, self.__EntranceY))

    def entrance_to_exit_y(self):
        y_diff = self.__ExitX - self.__EntranceX
        step = 1 if y_diff > 0 else -1
        for i in range(step, y_diff + step, step):
            if self.__Maze[self.__EntranceX + i][self.__EntranceY] == 0:
                self.__Maze[self.__EntranceX + i][self.__EntranceY] = 1
            self.__PathPositions.add((self.__EntranceX + i, self.__EntranceY))

    def entrance_to_exit_x(self):
        x_diff = self.__ExitY - self.__EntranceY
        step = 1 if x_diff > 0 else -1
        for i in range(step, x_diff + step, step):
            if self.__Maze[self.__ExitX][self.__EntranceY + i] == 0:
                self.__Maze[self.__ExitX][self.__EntranceY + i] = 1
            self.__PathPositions.add((self.__ExitX, self.__EntranceY + i))

    def pillars_to_path(self):
        for pillar_pos in self.__PillarPosition:
            nearest_path_pos = self.find_nearest_path(pillar_pos)
            self.create_path(pillar_pos, nearest_path_pos)

    def find_nearest_path(self, pillar_pos):
        # Implement logic to find the nearest path point from the pillar
        # This could use a simple distance calculation or a more complex pathfinding algorithm
        nearest_path_pos = min(self.__PathPositions, key=lambda path_pos: self.distance(pillar_pos, path_pos))
        return nearest_path_pos

    def create_path(self, start_pos, end_pos):
        # Create a path from start_pos to end_pos
        # Mark the path in the maze and add these positions to self.__PathPositions

        # Horizontal path
        step_x = 1 if end_pos[1] > start_pos[1] else -1
        for x in range(start_pos[1], end_pos[1] + step_x, step_x):
            if self.__Maze[start_pos[0]][x] == 0:
                self.__Maze[start_pos[0]][x] = 1
                self.__PathPositions.add((start_pos[0], x))

        # Vertical path
        step_y = 1 if end_pos[0] > start_pos[0] else -1
        for y in range(start_pos[0], end_pos[0] + step_y, step_y):
            if self.__Maze[y][end_pos[1]] == 0:
                self.__Maze[y][end_pos[1]] = 1
                self.__PathPositions.add((y, end_pos[1]))

    def distance(self, pos1, pos2):
        # Calculate the Manhattan distance between two points
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


    def get_Pill_Pos(self):
        print(f"Pillars : {self.__PillarPosition}")

    def get_Path_Pos(self):
        print(f"Paths : {self.__PathPositions}")

    def write_maze_to_file(self, file_name):
        with open(file_name, 'w') as file:
            file.write(self.__str__())

# Example usage
dungeon = Dungeon(7, 7)
dungeon.generate()
print(dungeon)
print(dungeon.get_Pill_Pos())
print(dungeon.get_Path_Pos())
dungeon.write_maze_to_file("Dungeon.txt")
