import unittest
from lab2.task4.src.binsearch import search
from utils import txt_to_list


class TestBinSearch(unittest.TestCase):

    def test_binsearch(self):
        search('Lab2/task4/txtf/input.txt', 'Lab2/task4/txtf/output.txt', 'Lab2/task4/txtf/info.txt')
        self.assertEqual(txt_to_list('Lab2/task4/txtf/output.txt'), [2, 0, -1, 0, -1])
