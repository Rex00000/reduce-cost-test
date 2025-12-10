import unittest
from calc import apply_discount
from calc import calculate_tax

class TestCalc(unittest.TestCase):

    def test_apply_discount(self):
        self.assertEqual(apply_discount(100, 0.1), 90)

    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            apply_discount(100, 1.5)

    def test_tax():
        self.assertEqual(calculate_tax(100, 0.05), 105)

if __name__ == "__main__":
    unittest.main()
