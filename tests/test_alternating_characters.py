import unittest
from hackerrank.alternating_characters import alternatingCharacters

class TestAlternatingCharacters(unittest.TestCase):
    def test_no_deletions_needed(self):
        # เทสกรณีที่ไม่ต้องลบเลย (ไม่เข้าเงื่อนไข if)
        self.assertEqual(alternatingCharacters("ABAB"), 0)

    def test_all_deletions_needed(self):
        # เทสกรณีที่ต้องลบทุกตัวที่ติดกัน (เข้าเงื่อนไข if ทุกรอบ)
        self.assertEqual(alternatingCharacters("AAAA"), 3)

    def test_mixed_deletions(self):
        self.assertEqual(alternatingCharacters("AAABBB"), 4)

if __name__ == '__main__':
    unittest.main()
