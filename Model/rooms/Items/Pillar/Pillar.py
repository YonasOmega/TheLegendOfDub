class Pillar():
    def __init__(self, pillar: str):
        self.pillar = pillar

    @property
    def pillar(self):
        return self.pillar

    @pillar.setter
    def pillar(self, value):
        self._pillar = value

