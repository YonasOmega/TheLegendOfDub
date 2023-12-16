class Pillar:
    """
    Represents a pillar in the game. Each pillar symbolizes a key concept of object-oriented programming.

    Attributes:
        __pillar (str): The name of the pillar.
    """

    def __init__(self, pillar: str):
        """
        Initializes a Pillar instance.

        Parameters:
            pillar (str): The name of the pillar.
        """
        self.__pillar = pillar

    @property
    def pillar(self):
        """
        Property to get the name of the pillar.

        Returns:
            str: The name of the pillar.
        """
        return self.__pillar

    @pillar.setter
    def pillar(self, value):
        """
        Property setter to set the name of the pillar.

        Parameters:
            value (str): The new name of the pillar.
        """
        self.__pillar = value

    def __str__(self):
        """
        String representation of the Pillar.

        Returns:
            str: The name of the pillar.
        """
        return f"{self.__pillar}"

