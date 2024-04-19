from .figure import Figure


class Triangle(Figure):
    def __init__(self, sides) -> None:
        super().__init__("Triangle", sides)
        self.a = sides[0]
        self.b = sides[1]
        self.c = sides[2]

    def calc_area(self):
        p = (self.a + self.b + self.c) / 2  # perimeter half
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def is_right_triangle(self):
        sides_copy = list.copy(self.sides)

        longest = max(sides_copy)
        idx_longest = sides_copy.index(longest)
        longest_squared = longest**2

        sides_copy.pop(idx_longest)
        shorter_squared_sum = sum(elem**2 for elem in sides_copy)

        return longest_squared == shorter_squared_sum
