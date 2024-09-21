import unittest

from src.calculator import sum, substract, multiply, division

class CalculatorTests(unittest.TestCase):

    def test_sum(self):
        assert sum(2, 3) == 5

    def test_substract(self):
        assert substract(5, 3) == 2

    def test_multiply(self):
        assert multiply(2, 3) == 6

    def test_division(self):
        assert division(10, 2) == 5

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            division(10, 0)
