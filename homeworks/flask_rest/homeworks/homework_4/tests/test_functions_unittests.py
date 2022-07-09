import unittest
from functions_to_test import Calculator

class TestForCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(7, 7), 14)
        self.assertEqual(Calculator.add(3, 5), 8)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(9, 4), 5)
        self.assertEqual(Calculator.subtract(11, 2), 9)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(6, 8), 48)
        self.assertEqual(Calculator.multiply(5, 6), 30)

    def test_divide(self):
        self.assertEqual(Calculator.divide(20, 5), 4)
        self.assertRaises(ValueError, lambda: Calculator.divide(8, 0))
        

if __name__ == '__main__':
    unittest.main()