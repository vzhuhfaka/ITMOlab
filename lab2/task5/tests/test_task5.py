import unittest
from lab2.task5.src.task5 import majority
from lab2.utils import read_line


class TestBinSearch(unittest.TestCase):

    def test_task5(self):
        majority('lab2/task5/txtf/input.txt', 'lab2/task5/txtf/output.txt', 'lab2/task5/txtf/info.txt')
        self.assertEqual(read_line('lab2/task5/txtf/output.txt'), '1')
