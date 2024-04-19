import unittest
from geomarea.utils.calc_util import CalcUtil
from geomarea.figures.triangle import Triangle


class test_calc(unittest.TestCase):
    SIDES_RIGHT = [3, 4, 5]
    SIDES_NOT_RIGHT = [3, 4, 6]
    SIDES_NOT_EXIST = [1, 2, 3, 4, 5]
    SIDES_NEGATIVE = [-1, 2, -3]
    RIGHT_TRIANGLE = Triangle(SIDES_RIGHT)
    NOT_RIGHT_TRIANGLE = Triangle(SIDES_NOT_RIGHT)

    def test_calc_area(self):
        self.assertEqual(round(CalcUtil.calc_area(5), 1), 78.5)
        self.assertEqual(CalcUtil.calc_area(3, 4, 5), 6.0)

    def test_invalid_sides(self):
        with self.assertRaises(ValueError):
            CalcUtil.calc_area(1, 2, 3, 4, 5)

    def test_right_triangle(self):
        self.assertTrue(self.RIGHT_TRIANGLE.is_right_triangle())
        self.assertFalse(self.NOT_RIGHT_TRIANGLE.is_right_triangle())

    def test_negative_sides(self):
        with self.assertRaises(ValueError):
            Triangle(self.SIDES_NEGATIVE)
