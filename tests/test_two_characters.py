import unittest
from hackerrank.two_characters import alternate

class TestTwoCharacters(unittest.TestCase):
    def test_valid_alternating_string(self):
        # เทสกรณีที่หาสตริงสลับกันได้ (เข้าเงื่อนไข if is_alt)
        self.assertEqual(alternate("beabeefeab"), 5)

    def test_no_valid_string(self):
        # เทสกรณีที่เป็นไปไม่ได้เลยที่จะได้สตริง 2 ชนิดสลับกัน
        self.assertEqual(alternate("aabaa"), 0)
        
    def test_short_string(self):
        # เทส Edge cases
        self.assertEqual(alternate("a"), 0)
        self.assertEqual(alternate("ab"), 2)

if __name__ == '__main__':
    unittest.main()
