from Model.rooms.Items.Pillar.Pillar import Pillar


class Encapsulation(Pillar):
    # do something
    def __init__(self):
        super().__init__("Encapsulation")


class Abstraction(Pillar):
    # do something
    def __init__(self):
        super().__init__("Abstraction")


class Inheritance(Pillar):
    # do something
    def __init__(self):
        super().__init__("Inheritance")


class Polymorphism(Pillar):
    # Do something
    def __init__(self):
        super().__init__("Polymorphism")


poly = Polymorphism()
print(poly.pillar)
poly.pillar = "value"
print(poly.pillar)
