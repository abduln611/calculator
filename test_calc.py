import unittest
from calc import Calc

class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negatives(self):
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_sub(self):
        self.assertEqual(self.calc.sub(2, 3), -1)

    def test_sub_zero(self):
        self.assertEqual(self.calc.sub(5, 5), 0)

    def test_mul(self):
        self.assertEqual(self.calc.mul(2, 3), 6)

    def test_mul_by_zero(self):
        self.assertEqual(self.calc.mul(5, 0), 0)

    def test_div(self):
        self.assertEqual(self.calc.div(6, 3), 2)

    def test_div_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.div(5, 0)


if __name__ == '__main__':
    unittest.main()