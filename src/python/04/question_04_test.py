from os import SEEK_HOLE
import unittest
from unittest.case import skip
from question_04 import answer_a, answer_b


class Question4(unittest.TestCase):
    def test_question_4a_trivial_input(self):
        self.assertEqual(answer_a("src/python/04/sample.txt"), 4512)

    @skip
    def test_question_4b_trivial_input(self):
        self.assertEqual(answer_b("src/python/04/sample.txt"), 240)

    def test_question_4a(self):
        self.assertEqual(answer_a("src/python/04/input.txt"), 54275)

    @skip
    def test_question_4b(self):
        self.assertEqual(answer_b("src/python/04/input.txt"), 1877149)


if __name__ == '__main__':
    unittest.main()
