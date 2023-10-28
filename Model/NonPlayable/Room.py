class Room():

    __item = 0
    __doors = 0
    __hasNPC = 0

    def __init__(self, item, doors, NPC):
        self.__item = item
        self.__doors = doors
        self.__hasNPC = NPC

    def hasItem(self):
        if self.__item != 0:
            return True
        return False

    def placeEnemy(self):
        if self.__hasNPC != 0:
            return self.__hasNPC
        return False
