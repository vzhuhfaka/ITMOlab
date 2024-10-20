import unittest
from Lab2.task5.src.majority import majority


def txt_to_str(file_txt):
    with open(file_txt, 'r') as f:
        return f.readline()


class TestBinSearch(unittest.TestCase):

    def test_binsearch(self):
        majority('Lab2/task5/tests/files/input.txt', 'Lab2/task5/tests/files/output.txt', 'Lab2/task5/tests/files/info.txt')
        self.assertEqual(txt_to_str('Lab2/task5/tests/files/output.txt'), '1')
