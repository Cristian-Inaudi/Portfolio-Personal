from random import randint

class Die:
    """Una clase que representa a un dado."""

    def __init__(self, num_sides=6):
        """Asume un dado de 6 caras."""
        self.num_sides = num_sides

    def roll(self):
        """Retorna un valor random entre 1 y el numero de caras."""
        return randint(1, self.num_sides)
