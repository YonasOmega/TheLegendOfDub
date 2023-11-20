import random

class Dungeon():
    __gridWidth = 0
    __gridHeight = 0
    __grid = 0
    __entrance = 0
    __Exit = 0

    def __init__(self, width, height):
        self.__gridWidth = width
        self.__gridHeight = height
        self.__grid = [[0 for _ in range(self.__gridWidth)] for _ in range(self.__gridHeight)]
        self.__entrance =  self.__grid[random.randint(0, self.__gridWidth)][random.randint(0, self.__gridHeight)]
        self.__Exit = self.__grid[random.randint(0, self.__gridWidth)][random.randint(0, self.__gridHeight)]
        self.different_entrance_and_exit(self)

    def different_entrance_and_exit(self):
        if self.__entrance == self.__Exit:
            self.__entrance = self.__grid[random.randint(0, self.__gridWidth)][random.randint(0, self.__gridHeight)]
            self.__Exit = self.__grid[random.randint(0, self.__gridWidth)][random.randint(0, self.__gridHeight)]
            self.different_entrance_and_exit()

