from calculator.calculator import Calculator
import pytest
class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected
    def test_subtract(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 3087
        assert result == expected
    def test_multiply(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 5332114
        assert result == expected
    def test_divide(self):
        # arrange
        a = 5000
        b = 20
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 250
        assert result == expected
    def test_divide_zero_a(self):
        # arrange
        a = 0
        b = 20
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 0
        assert result == expected
    def test_divide_zero_b(self):
        # arrange
        a = 5000
        b = 0
        cal = Calculator()

        # act & assert
        with pytest.raises(ZeroDivisionError):
            cal.divide(a, b)
