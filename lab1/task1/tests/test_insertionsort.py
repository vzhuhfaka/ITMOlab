import unittest
from lab1.task1.src.insertionsort import insertionsort
from utils import txt_to_list


class TestInsertionSort(unittest.TestCase):

    def test_insertionsort(self):
        insertionsort('lab1/task1/txtf/test_input.txt', 'lab1/task1/txtf/test_output.txt', 'lab1/task1/txtf/test_info.txt')
        self.assertEqual(txt_to_list('lab1/task1/txtf/test_output.txt'), [26, 31, 41, 41, 58, 59])
