import unittest
from hackerrank.funny_string import funnyString

class TestFunnyString(unittest.TestCase):
    def test_funny_string(self):
        # เทสกรณีที่สตริงมีความ "Funny" (รันจบและ return "Funny")
        self.assertEqual(funnyString("acxz"), "Funny")

    def test_not_funny_string(self):
        # เทสกรณีที่สตริง "Not Funny" (เข้าเงื่อนไข if diff1 != diff2)
        self.assertEqual(funnyString("bcxz"), "Not Funny")

if __name__ == '__main__':
    unittest.main()
