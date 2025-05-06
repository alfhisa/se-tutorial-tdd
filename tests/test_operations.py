import unittest
from calculator.operations import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(7, 3), 4)
        self.assertEqual(subtract(5, 10), -5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 2), 6)
        self.assertEqual(multiply(7, 3), 21)
        self.assertEqual(multiply(5, -10), -50)

    def test_divide(self):
        self.assertEqual(divide(4, 2), 2)
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(5, 5), 1)

if __name__ == '__main__':
    unittest.main()
