import unittest
from lab2.task1.src.task1 import main
from lab2.utils import txt_to_list


class TestMegreSearch(unittest.TestCase):

    def test_mergesort(self):
        main('lab2/task1/txtf/input.txt', 'lab2/task1/txtf/output.txt', 'lab2/task1/txtf/info.txt')
<<<<<<< HEAD
=======

>>>>>>> 257067c (refactor)
        self.assertEqual(txt_to_list('lab2/task1/txtf/output.txt'), [0, 1, 2, 4, 6])
