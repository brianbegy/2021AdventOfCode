from os import SEEK_HOLE
import unittest
from unittest.case import skip
from question_06 import answer_a, answer_b


class Question6(unittest.TestCase):
    def test_question_6a_trivial_input(self):
        self.assertEqual(answer_a("src/python/06/sample.txt"), 5934)

    def test_question_6b_trivial_input(self):
        self.assertEqual(answer_b("src/python/06/sample.txt"), 26984457539)

    @skip
    def test_question_6a(self):
        self.assertEqual(answer_a("src/python/06/input.txt"), 388739)

    @skip
    def test_question_6b(self):
        self.assertEqual(answer_b("src/python/06/input.txt"), 17717)


if __name__ == '__main__':
    unittest.main()
