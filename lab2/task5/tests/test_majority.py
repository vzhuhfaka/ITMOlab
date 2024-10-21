import unittest
from lab2.task5.src.majority import majority
from utils import txt_to_str


class TestBinSearch(unittest.TestCase):

    def test_binsearch(self):
        majority('Lab2/task5/txtf/input.txt', 'Lab2/task5/txtf/output.txt', 'Lab2/task5/txtf/info.txt')
        self.assertEqual(txt_to_str('Lab2/task5/txtf/output.txt'), '1')
