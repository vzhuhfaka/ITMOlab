import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
sys.path.insert(0, parent_dir)

from lab7.utils import read_data, write_data


def distance(s1: str, s2: str) -> int:
    s1_len = len(s1)
    s2_len = len(s2)

    D = [[0] * (s2_len + 1) for _ in range(s1_len + 1)]  # создаём двумерный массив

    # Базовые случаи
    for i in range(s1_len + 1):
        D[i][0] = i
    for j in range(s2_len + 1):
        D[0][j] = j

    # Заполнение таблицы
    for i in range(1, s1_len + 1):
        for j in range(1, s2_len + 1):
            if s1[i - 1] == s2[j - 1]:
                D[i][j] = D[i - 1][j - 1]  # берётся значение из диагональной ячейки
            else:
                D[i][j] = 1 + min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1])  # min(удаление, вставка, замена)

    return D[-1][-1]


def task2():
    PATH_INPUT = 'lab7/task3/txtf/input.txt'
    PATH_OUTPUT = 'lab7/task3/txtf/output.txt'

    origin_input = read_data(PATH_INPUT)

    data_ = read_data(PATH_INPUT)
    word_1 = data_[0]
    word_2 = data_[1]

    result = distance(word_1, word_2)

    write_data(PATH_OUTPUT, str(result))
    print(origin_input)
    print(result)


if __name__ == "__main__":
    task2()
