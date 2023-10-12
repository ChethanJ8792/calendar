import unittest

def add_numbers(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_positive_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        result = add_numbers(-2, -3)
        self.assertEqual(result, -5)

    def test_mixed_numbers(self):
        result = add_numbers(2, -3)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()
