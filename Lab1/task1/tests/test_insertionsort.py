import unittest
from Lab1.task1.src.insertionsort import insertionsort

def txt_to_list(file_txt):
    res = []
    with open(file_txt, 'r') as f:
        for i in f.readline().split():
            res.append(int(i))
    return res


class TestInsertionSort(unittest.TestCase):

    def test_insertionsort(self):
        insertionsort('Lab1/task1/tests/test_input.txt', 'Lab1/task1/tests/test_output.txt', 'Lab1/task1/tests/test_info.txt')
        self.assertEqual(txt_to_list('Lab1/task1/tests/test_output.txt'), [26, 31, 41, 41, 58, 59])
