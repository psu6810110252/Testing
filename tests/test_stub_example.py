import unittest
from unittest.mock import patch
from coe_number.number_utils import is_prime_list

# สมมติว่ามีฟังก์ชัน get_numbers_from_api() ที่เรายังเขียนไม่เสร็จ หรือต่อเน็ตไม่ได้
def get_numbers_from_api():
    # โค้ดจริงอาจจะใช้ requests.get('...')
    pass

# สมมติว่านี่คือฟังก์ชันที่ต้องไปดึงข้อมูลจากระบบอื่น ซึ่งเราจะจำลองมัน
def fetch_data_and_check_prime():
    numbers = get_numbers_from_api() 
    return is_prime_list(numbers)


class StubTest(unittest.TestCase):
    
    # ใช้ @patch เพื่อทำ Stub ฟังก์ชัน get_numbers_from_api
    @patch('test_stub_example.get_numbers_from_api')
    def test_fetch_data_with_stub(self, mock_get_numbers):
        # กำหนดค่าที่ต้องการให้ Stub จำลองและส่งกลับมา
        mock_get_numbers.return_value = [2, 3, 5, 7]
        
        # ทดสอบการทำงาน
        result = fetch_data_and_check_prime()
        
        # คาดหวังว่าต้องเป็น True เพราะข้อมูลจาก Stub เป็นจำนวนเฉพาะทั้งหมด
        self.assertTrue(result)
        # ตรวจสอบว่าฟังก์ชันจำลองถูกเรียกใช้งานจริงๆ
        mock_get_numbers.assert_called_once()
    
    @patch('test_stub_example.get_numbers_from_api')
    def test_fetch_data_with_stub_composite(self, mock_get_numbers):
        mock_get_numbers.return_value = [2, 3, 4, 7]
        result = fetch_data_and_check_prime()
        self.assertFalse(result)
        mock_get_numbers.assert_called_once()

if __name__ == '__main__':
    unittest.main()
