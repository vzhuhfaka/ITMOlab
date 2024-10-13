import unittest
from Lab2.task3.src.binsum import main_binsum


def txt_to_str(file_txt):
    with open(file_txt, 'r') as f:
        return f.readline()


class TestBinSum(unittest.TestCase):

    def test_binsum(self):
        main_binsum('test_input.txt', 'test_output.txt')
        self.assertEqual(txt_to_str('test_output.txt'), '111')