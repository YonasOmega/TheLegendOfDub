from Model.rooms.Items.Pillar.Pillar import Pillar

class Encapsulation(Pillar):
    """
    Represents the Encapsulation pillar in the dungeon game.
    """

    def __init__(self):
        super().__init__("Encapsulation")


class Abstraction(Pillar):
    """
    Represents the Abstraction pillar in the dungeon game.
    """

    def __init__(self):
        super().__init__("Abstraction")


class Inheritance(Pillar):
    """
    Represents the Inheritance pillar in the dungeon game.
    """

    def __init__(self):
        super().__init__("Inheritance")


class Polymorphism(Pillar):
    """
    Represents the Polymorphism pillar in the dungeon game.
    """

    def __init__(self):
        super().__init__("Polymorphism")


# Example usage
# poly = Polymorphism()
# print(poly.pillar)
# poly.pillar = "value"
# print(poly.pillar)
