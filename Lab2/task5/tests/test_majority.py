import unittest
from Lab2.task5.src.majority import majority
from utils import txt_to_str


class TestBinSearch(unittest.TestCase):

    def test_binsearch(self):
        majority('Lab2/task5/tests/files/input.txt', 'Lab2/task5/tests/files/output.txt', 'Lab2/task5/tests/files/info.txt')
        self.assertEqual(txt_to_str('Lab2/task5/tests/files/output.txt'), '1')
