import unittest
from lab1.task3.src.binsum import main_binsum
from utils import txt_to_str


class TestBinSum(unittest.TestCase):

    def test_binsum(self):
        main_binsum('Lab1/task3/txtf/test_input.txt', 'Lab1/task3/txtf/test_output.txt', 'Lab1/task3/tests/test_time.txt')
        self.assertEqual(txt_to_str('Lab1/task3/txtf/test_output.txt'), '11101')
