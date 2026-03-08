import unittest
from unittest.mock import MagicMock
from coe_number.number_utils import is_random_number_prime, NumberGeneratorService

class TestStubExample(unittest.TestCase):
    def test_is_random_number_prime_with_stub_prime(self):
        # 1. Create a stub for the NumberGeneratorService using Mock
        stub_service = NumberGeneratorService()
        
        # 2. Stub the fetch_random_number method to always return a prime number (e.g., 7)
        # We don't want to actually wait for time.sleep or get random numbers in our tests!
        stub_service.fetch_random_number = MagicMock(return_value=7)
        
        # 3. Test the function using our stub
        result = is_random_number_prime(stub_service)
        
        # 4. Assertions
        self.assertTrue(result)
        stub_service.fetch_random_number.assert_called_once()

    def test_is_random_number_prime_with_stub_composite(self):
        # 1. Create a stub for the NumberGeneratorService
        stub_service = NumberGeneratorService()
        
        # 2. Stub the fetch_random_number method to always return a composite number (e.g., 10)
        stub_service.fetch_random_number = MagicMock(return_value=10)
        
        # 3. Test the function using our stub
        result = is_random_number_prime(stub_service)
        
        # 4. Assertions
        self.assertFalse(result)
        stub_service.fetch_random_number.assert_called_once()

if __name__ == '__main__':
    unittest.main()
