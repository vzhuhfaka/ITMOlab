import unittest
from Lab2.task1.src.insertionsort import insertionsort

def txt_to_list(file_txt):
    res = []
    with open(file_txt, 'r') as f:
        for i in f.readline().split():
            res.append(int(i))
    return res


class TestInsertionSort(unittest.TestCase):

    def test_insertionsort(self):
        insertionsort('test_input.txt', 'test_output.txt', 'test_info.txt')
        self.assertEqual(txt_to_list('test_output.txt'), [26, 31, 41, 41, 58, 59])
