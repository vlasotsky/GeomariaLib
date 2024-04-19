class SideValidator:

    @staticmethod
    def validate_sides(sides: list):
        if not all(side > 0 for side in sides):
            raise ValueError("A side can't be negative")
