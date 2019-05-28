"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_zeros(self):
        assert 0 == calculator.add(0,0)

    def test_negs(self):
        assert -2 == calculator.add(-1,-1)

    def test_addition(self):
        assert 9 == calculator.add(4, 5)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_sumation(self):
        assert 3 == calculator.sum_numbers(1,1,1)

    def test_multiplication(self):
        assert 4 == calculator.multiply_numbers(1,2,2)