import unittest
from hackerrank.grid_challenge import gridChallenge

class TestGridChallenge(unittest.TestCase):
    def test_valid_grid(self):
        # เทสกรณีที่เรียงได้สมบูรณ์ทั้งแนวนอนและตั้ง
        grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_invalid_grid(self):
        # เทสกรณีที่เรียงแนวนอนแล้ว แต่แนวตั้งไม่เรียง (เข้าเงื่อนไข if แล้ว return NO)
        grid = ["mpxz", "abcd", "wlmf"]
        self.assertEqual(gridChallenge(grid), "NO")

if __name__ == '__main__':
    unittest.main()
