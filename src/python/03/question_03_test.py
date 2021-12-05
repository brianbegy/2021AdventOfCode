from os import SEEK_HOLE
import unittest
from unittest.case import skip
from question_03 import answer_a, answer_b


class Question3(unittest.TestCase):

    def test_question_3a_trivial_input(self):
        self.assertEqual(answer_a("src/python/03/sample.txt"), 198)

    def test_question_3b_trivial_input(self):
        self.assertEqual(answer_b("src/python/03/sample.txt"), 230)

    def test_question_3a(self):
        self.assertEqual(answer_a("src/python/03/input.txt"), 2003336)

    def test_question_3b(self):
        self.assertEqual(answer_b("src/python/03/input.txt"), 1877139)


if __name__ == '__main__':
    unittest.main()
