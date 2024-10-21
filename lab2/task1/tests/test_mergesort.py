import unittest
from lab2.task1.src.mergesort import main
from lab2.utils import txt_to_list


class TestMegreSearch(unittest.TestCase):

    def test_mergesort(self):
        main('Lab2/task1/txtf/input.txt', 'Lab2/task1/txtf/output.txt', 'Lab2/task1/txtf/info.txt')
        self.assertEqual(txt_to_list('Lab2/task1/txtf/output.txt'), [0, 1, 2, 4, 6])
