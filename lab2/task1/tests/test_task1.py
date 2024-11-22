import unittest
from lab2.task1.src.task1 import main
from lab2.utils import read_lines, write_in_file, write_info


class TestMegreSearch(unittest.TestCase):

    def test_mergesort(self):
        path_input = 'lab2/task1/txtf/input.txt'
        path_output = 'lab2/task1/txtf/output.txt'
        path_info = 'lab2/task1/txtf/info.txt'
        input_data = read_lines(path_input)

        ans = main(input_data)

        write_info(path_info, main, input_data)
        write_in_file(path_output, ans)
        self.assertEqual(ans, [0, 1, 2, 4, 6])
