import unittest
from Lab2.task4.src.binsearch import search


def txt_to_list(file_txt):
    res = []
    with open(file_txt, 'r') as f:
        for i in f.readline().split():
            res.append(int(i))
    return res


class TestBinSearch(unittest.TestCase):

    def test_binsearch(self):
        search('Lab2/task4/tests/files/input.txt', 'Lab2/task4/tests/files/output.txt', 'Lab2/task4/tests/files/info.txt')
        self.assertEqual(txt_to_list('Lab2/task4/tests/files/output.txt'), [2, 0, -1, 0, -1])
