import unittest
from lab2.task5.src.task5 import majority
from lab2.utils import txt_to_str


class TestBinSearch(unittest.TestCase):

    def test_binsearch(self):
        majority('lab2/task5/txtf/input.txt', 'lab2/task5/txtf/output.txt', 'lab2/task5/txtf/info.txt')
        self.assertEqual(txt_to_str('lab2/task5/txtf/output.txt'), '1')
