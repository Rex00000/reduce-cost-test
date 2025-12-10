import unittest
from calc import apply_discount

class TestCalc(unittest.TestCase):

    def test_apply_discount(self):
        self.assertEqual(apply_discount(100, 0.1), 90)

    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            apply_discount(100, 1.5)

if __name__ == "__main__":
    unittest.main()
