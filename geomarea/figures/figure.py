from geomarea.utils.side_validator import SideValidator as sv


class Figure:
    def __init__(self, name="Anonimous figure", sides=None) -> None:
        sv.validate_sides(sides)

        self.name = name
        self.sides = sides

    def calc_area(self):
        pass

    def get_sides(self):
        return self.sides
