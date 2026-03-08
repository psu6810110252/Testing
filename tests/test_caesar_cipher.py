import unittest
from hackerrank.caesar_cipher import caesarCipher

class TestCaesarCipher(unittest.TestCase):
    def test_lowercase_shift(self):
        # เทสการเลื่อนตัวพิมพ์เล็ก (เข้าเงื่อนไข islower)
        self.assertEqual(caesarCipher("xyz", 3), "abc")

    def test_uppercase_shift(self):
        # เทสการเลื่อนตัวพิมพ์ใหญ่ (เข้าเงื่อนไข isupper)
        self.assertEqual(caesarCipher("XYZ", 3), "ABC")

    def test_symbols_no_shift(self):
        # เทสสัญลักษณ์ (เข้าเงื่อนไข else)
        self.assertEqual(caesarCipher("a-b-c", 2), "c-d-e")

    def test_large_k(self):
        # เทสกรณี k มากกว่า 26
        self.assertEqual(caesarCipher("abc", 28), "cde")

if __name__ == '__main__':
    unittest.main()
