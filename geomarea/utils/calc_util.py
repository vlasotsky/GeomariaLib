from geomarea.figures.circle import Circle
from geomarea.figures.triangle import Triangle


class CalcUtil:

    @staticmethod
    def calc_area(*sides):
        num_sides = len(sides)

        if num_sides == 1:
            figure_type = Circle(sides)
        elif num_sides == 3:
            figure_type = Triangle(sides)
        else:
            raise ValueError("Invalid number of sides or no such figure in database")

        return figure_type.calc_area()
