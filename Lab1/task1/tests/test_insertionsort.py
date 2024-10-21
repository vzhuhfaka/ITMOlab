import unittest
from Lab1.task1.src.insertionsort import insertionsort
from utils import txt_to_list


class TestInsertionSort(unittest.TestCase):

    def test_insertionsort(self):
        insertionsort('Lab1/task1/tests/test_input.txt', 'Lab1/task1/tests/test_output.txt', 'Lab1/task1/tests/test_info.txt')
        self.assertEqual(txt_to_list('Lab1/task1/tests/test_output.txt'), [26, 31, 41, 41, 58, 59])
