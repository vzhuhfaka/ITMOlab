import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
sys.path.insert(0, parent_dir)

from lab1.utils import read_lines, write_in_file


def insertionsort(ar):
    for i in range(1, len(ar)):
        value = ar[i]
        j = i - 1
        while value < ar[j] and j >= 0:
            ar[j+1] = ar[j]
            j -= 1
        ar[j+1] = value
    return ar


def task1():
    path_input = 'lab1/task1/txtf/input.txt'
    path_output = 'lab1/task1/txtf/output.txt'

    array = read_lines(path_input)[1]  # берём вторую строчку, так как в первой число элементов
    sorted_array = insertionsort(array)

    write_in_file(path_output, sorted_array)
    print(sorted_array)


if __name__ == '__main__':
    task1()