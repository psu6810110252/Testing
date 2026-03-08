import unittest
from coe_number.number_utils import is_prime, calculate_average

class TestNumberUtils(unittest.TestCase):
    # Tests for is_prime
    def test_is_prime_valid_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(97))

    def test_is_prime_composites(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(100))
        self.assertFalse(is_prime(9))

    def test_is_prime_edge_cases(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(-5))

    def test_is_prime_type_error(self):
        with self.assertRaises(TypeError):
            is_prime("2")
        with self.assertRaises(TypeError):
            is_prime(3.14)

    # Tests for calculate_average
    def test_calculate_average_valid(self):
        self.assertEqual(calculate_average([1, 2, 3]), 2.0)
        self.assertEqual(calculate_average([10, 20, 30, 40]), 25.0)

    def test_calculate_average_empty(self):
        self.assertEqual(calculate_average([]), 0.0)

    def test_calculate_average_type_error(self):
        with self.assertRaises(TypeError):
            calculate_average("123")
            
    def test_calculate_average_value_error(self):
        with self.assertRaises(ValueError):
            calculate_average([1, 2, "3"])

if __name__ == '__main__':
    unittest.main()
