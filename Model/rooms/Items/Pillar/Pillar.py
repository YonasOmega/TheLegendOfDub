class Pillar:
    def __init__(self, pillar: str):
        self.__pillar = pillar

    @property
    def pillar(self):
        return self.__pillar

    @pillar.setter
    def pillar(self, value):
        self.__pillar = value

