import unittest
from coe_number.number_utils import is_prime_list

class PrimeListTest(unittest.TestCase):
    
    # 1. เทสกรณีที่เป็นจำนวนเฉพาะทั้งหมด
    def test_all_primes(self):
        prime_list = [2, 3, 5, 7, 11]
        self.assertTrue(is_prime_list(prime_list))
        
    # 2. เทสกรณีที่มีเลข 1 ผสมอยู่ (Edge case: 1 ไม่ใช่จำนวนเฉพาะ)
    def test_contains_one_is_not_prime(self):
        prime_list = [1, 2, 3]
        self.assertFalse(is_prime_list(prime_list))
        
    # 3. เทสกรณีที่มีเลขจำนวนเต็มลบ และ 0
    def test_negative_and_zero_is_not_prime(self):
        prime_list = [-5, 0, 2]
        self.assertFalse(is_prime_list(prime_list))
        
    # 4. เทสกรณีที่มีจำนวนประกอบ (Composite number) เช่น 4, 9 ผสมอยู่
    def test_contains_composite_number(self):
        prime_list = [2, 3, 4, 5]
        self.assertFalse(is_prime_list(prime_list))
        
    # 5. เทสกรณีเป็นลิสต์ว่าง (มักจะให้ค่าเป็น True เพราะไม่มีตัวไหนผิดเงื่อนไข)
    def test_empty_list(self):
        prime_list = []
        self.assertTrue(is_prime_list(prime_list))

    # 6. เทสกรณีที่มีตัวเลขเยอะๆ (Large primes)
    def test_large_primes(self):
        prime_list = [97, 101, 103]
        self.assertTrue(is_prime_list(prime_list))

if __name__ == '__main__':
    unittest.main()
