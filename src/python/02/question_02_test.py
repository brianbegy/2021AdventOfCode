import unittest
from unittest.case import skip
from question_02 import answer


class Question1(unittest.TestCase):
    def test_question_2a_trivial_input(self):
        self.assertEqual(answer("src/python/02/sample.txt"), 150)

    def test_question_2b_trivial_input(self):
        self.assertEqual(answer("src/python/02/sample.txt", True), 900)

    def test_question_2a(self):
        self.assertEqual(answer("src/python/02/input.txt"), 1989014)

    def test_question_2b(self):
        self.assertEqual(answer("src/python/02/input.txt", True), 2006917119)


if __name__ == '__main__':
    unittest.main()
