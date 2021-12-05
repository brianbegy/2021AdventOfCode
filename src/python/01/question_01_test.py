import unittest
from question_01 import answer


class Question1(unittest.TestCase):
    def test_question_1a_trivial_input(self):
        self.assertEqual(answer("src/python/01/sample.txt", 1), 7)

    def test_question_1b_trivial_input(self):
        self.assertEqual(answer("src/python/01/sample.txt", 3), 5)

    def test_question_1a(self):
        self.assertEqual(answer("src/python/01/input.txt", 1), 1527)

    def test_question_1b(self):
        self.assertEqual(answer("src/python/01/input.txt", 3), 1575)


if __name__ == '__main__':
    unittest.main()
