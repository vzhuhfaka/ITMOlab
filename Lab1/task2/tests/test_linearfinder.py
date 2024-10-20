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
        linearfinder('Lab1/task2/tests/test_input.txt', 'Lab1/task2/tests/test_output.txt')
        self.assertEqual(txt_to_list('Lab1/task2/tests/test_output.txt'), ['3', '9'])