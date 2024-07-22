import unittest

from summer import sum_scores

class TestSumScores(unittest.TestCase): # Python OOP

    def test_sum_empty(self):
        self.assertEqual(sum_scores([]), 0)

    def test_sum_numbers(self):
        self.assertEqual(sum_scores([8, 9, 7]), 24)