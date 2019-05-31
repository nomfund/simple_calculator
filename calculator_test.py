"""
Unit tests for the calculator library
"""
import calculator

class TestCalculator:

    def test_zeros(self):
        assert 0 == calculator.sum_numbers(0,0)

    def test_negs(self):
        assert -2 == calculator.sum_numbers(-1,-1)

    def test_addition(self):
        assert 10 == calculator.sum_numbers(1,2,3,4)

    def test_sumation(self):
        assert 3 == calculator.sum_numbers(1,2)

    def test_multiplication(self):
        assert 24 == calculator.multiply_numbers(1,2,3,4)
        
    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)