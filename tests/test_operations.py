import unittest
from calculator.function import add, sub, div, mul

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_sub(self):
        self.assertEqual(sub(2, 3), -1)
        self.assertEqual(sub(-1, 1), -2)
        self.assertEqual(sub(0, 0), 0)

    def test_div(self):
        self.assertEqual(div(4, 2), 2)
        self.assertEqual(div(10, 5), 2)
        self.assertEqual(div(1, 1), 1)

    def test_mul(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-1, 1), -1)
        self.assertEqual(mul(0, 0), 0)

if __name__ == '__main__':
    unittest.main()