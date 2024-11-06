import unittest
from lab2.task4.src.task4 import search
from lab2.utils import txt_to_list


class TestBinSearch(unittest.TestCase):

    def test_binsearch(self):
        search('lab2/task4/txtf/input.txt', 'lab2/task4/txtf/output.txt', 'lab2/task4/txtf/info.txt')
        self.assertEqual(txt_to_list('lab2/task4/txtf/output.txt'), [2, 0, -1, 0, -1])
