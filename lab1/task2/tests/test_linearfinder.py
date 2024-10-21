import unittest
from lab1.task2.src.linearfinder import linearfinder
from utils import txt_to_numlist


class TestLinearFinder(unittest.TestCase):

    def test_linearfinder(self):
        linearfinder('Lab1/task2/tests/test_input.txt', 'Lab1/task2/tests/test_output.txt')
        self.assertEqual(txt_to_numlist('Lab1/task2/tests/test_output.txt'), ['3', '9'])