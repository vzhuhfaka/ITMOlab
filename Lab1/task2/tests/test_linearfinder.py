import unittest
from Lab1.task2.src.linearfinder import linearfinder

def txt_to_list(file_txt):
    res = []
    with open(file_txt, 'r') as f:
        for i in f.readline():
            if i in '0123456789':
                res.append(i)
    return res


class TestLinearFinder(unittest.TestCase):

    def test_linearfinder(self):
        linearfinder('test_input.txt', 'test_output.txt')
        self.assertEqual(txt_to_list('test_output.txt'), ['3', '9'])