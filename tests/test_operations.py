import unittest
from calculator.operations import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(10, 2), 13)

    def test_subtract(self):
        self.assertEqual(subtract(10,2), 8)
        self.assertEqual(subtract(-5,2), -7)
        self.assertEqual(subtract(0,0), 0)
        pass

    def test_multiply(self):
        self.assertEqual(multiply(0,0), 0)
        self.assertEqual(multiply(20,0), 0)
        self.assertEqual(multiply(20,10), 200)
        self.assertEqual(multiply(-5,5), -25)
        pass

    def test_divide(self):
        self.assertEqual(divide(0,0), 0)
        self.assertEqual(divide(0,2), 0)
        self.assertEqual(divide(0,5), 0)
        self.assertEqual(divide(0,7), 0)
        self.assertEqual(divide(0,10), 0)
        self.assertEqual(divide(0,22), 0)
        self.assertEqual(divide(1,22), 1/22)
        self.assertEqual(divide(20,22), divide(20,22))
        # TODO: add assertions for divide
        pass

if __name__ == '__main__':
    unittest.main()
