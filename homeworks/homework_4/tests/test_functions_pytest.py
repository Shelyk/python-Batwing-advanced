import pytest
from functions_to_test import Calculator

class TestForCalculator():

    def test_add(self):
        assert Calculator.add(7, 7) == 14
        assert Calculator.add(3, 5) == 8

    def test_subtract(self):
        assert Calculator.subtract(9, 4) == 5
        assert Calculator.subtract(11, 2) == 9

    def test_multiply(self):
        assert Calculator.multiply(6, 8) == 48
        assert Calculator.multiply(5, 6) == 30

    def test_divide(self):
        assert Calculator.divide(20, 5) == 4
        with pytest.raises(ValueError) as e:
            Calculator.divide(8, 0)
        assert "Can not divide by zero!" in str(e.value)

if __name__ == '__main__':
    pytest.main()