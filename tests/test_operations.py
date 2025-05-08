import unittest
from calculator.operations import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        # TODO: add assertions for subtract
        pass

    def test_multiply(self):
        # TODO: add assertions for multiply
        pass

    def test_divide(self):
        # TODO: add assertions for divide
        pass

if __name__ == '__main__':
    unittest.main()
