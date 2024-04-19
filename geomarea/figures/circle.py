from math import pi
from .figure import Figure


class Circle(Figure):
    def __init__(self, sides) -> None:
        super().__init__("Circle", sides)
        self.radius = sides[0]

    def calc_area(self):
        return pi * self.radius ** 2
