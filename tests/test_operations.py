import unittest
from calculator.operations import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        # TODO: add assertions for subtract
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        pass

    def test_multiply(self):
        # TODO: add assertions for multiply
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(0, 5), 0)
        pass

    def test_divide(self):
       self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            divide(5, 0)
        pass

if __name__ == '__main__':
    unittest.main()
