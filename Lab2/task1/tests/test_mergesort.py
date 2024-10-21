import unittest
from Lab2.task1.src.mergesort import main
from utils import txt_to_list


class TestMegreSearch(unittest.TestCase):

    def test_mergesort(self):
        main('Lab2/task1/tests/files/input.txt', 'Lab2/task1/tests/files/output.txt', 'Lab2/task1/tests/files/info.txt')
        self.assertEqual(txt_to_list('Lab2/task1/tests/files/output.txt'), [0, 1, 2, 4, 6])
