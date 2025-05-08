import unittest
from calculator.operations import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(subtract(4, 1), 3)
        self.assertEqual(multiply(2, 1), 2)
        self.assertEqual(divide(2, 0), 'undefined')

if __name__ == '__main__':
    unittest.main()