from os import SEEK_HOLE
import unittest
from unittest.case import skip
from question_05 import answer_a, answer_b


class Question5(unittest.TestCase):
    def test_question_5a_trivial_input(self):
        self.assertEqual(answer_a("src/python/05/sample.txt"), 5)

    def test_question_5b_trivial_input(self):
        self.assertEqual(answer_b("src/python/05/sample.txt"), 12)

    def test_question_5a(self):
        self.assertEqual(answer_a("src/python/05/input.txt"), 4728)

    def test_question_5b(self):
        self.assertEqual(answer_b("src/python/05/input.txt"), 17717)


if __name__ == '__main__':
    unittest.main()
