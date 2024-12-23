import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
sys.path.insert(0, parent_dir)

from lab6.utils import read_data, write_data


def hash_function(obj, size_hash_table):
    """
    Хеш-функция, которая считает сумму кодов символов и
    возвращает остаток от деления на размер хеш-таблицы

    Пример: hash_function('abc', 10) -> 4
    """
    sum_chars = sum([ord(i) for i in obj])
    return sum_chars % size_hash_table


def usa_elections(data, hash_table):
    """
    Заполняет хеш-таблицу и, используя хеш-функцию, вставляет в нее данные

    Пример входных данных: data=[['A', '1'], ['B', '2'], ['C', '3']]
                           hash_table=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    Пример выходных данных: hash_table=[[0, 'A', 1], [1, 'B', 2], [2, 'C', 3]]
    """
    size_hash_table = len(hash_table)
    for i in data:
        name_id = hash_function(i[0], size_hash_table)

        # если такой кандидат уже есть в хеш-таблице
        if hash_table[name_id] != [0, 0, 0]:

            # если такой кандидат уже есть в хеш-таблице
            if name_id == hash_table[name_id][0] and i[0] == hash_table[name_id][1]:
                hash_table[name_id][2] += int(i[1])
            else:

                # ищем свободное место, чтобы избавится от коллизии
                while hash_table[name_id] != [0, 0, 0]:
                    name_id = (name_id + 1) % size_hash_table
                else:
                    hash_table[name_id] = [name_id, i[0], int(i[1])]

        else:
            # добавляем новую запись в хеш-таблицу
            hash_table[name_id] = [name_id, i[0], int(i[1])]

    return hash_table


def main(data):
    """
    Функция для решения задачи, которая заполняет хеш-таблицу и возвращает
    список кандидатов и их количество голосов

    Пример входных данных: [['McCain', '10'], ['McCain', '5'], ['Obama', '9'], ['Obama', '8'], ['McCain', '1']]
    Пример выходных данных: [['McCain', 16], ['Obama', 17]]
    """
    hash_table_ = [[0, 0, 0] for i in range(10)]
    usa_elections(data, hash_table_)
    candidates = []

    # находим уникальных кандидатов
    for i in data:
        name_id = hash_function(i[0], len(hash_table_))
        candidate = hash_table_[name_id][1]
        if candidate not in candidates:
            candidates.append(candidate)

    # находим количество голосов кандидатов
    for i in range(len(candidates)):
        name_id = hash_function(candidates[i], len(hash_table_))
        votes = hash_table_[name_id][2]
        candidates[i] = [candidates[i], votes]

    return sorted(candidates, key=lambda x: x[0])  # сортировка в лексикографическом порядке


def task5():
    PATH_INPUT = 'lab6/task5/txtf/input.txt'
    PATH_OUTPUT = 'lab6/task5/txtf/output.txt'

    data_ = [i.strip().split() for i in read_data(PATH_INPUT)]
    result = main(data_)

    write_data(PATH_OUTPUT, '\n'.join([f'{i[0]} {i[1]}' for i in result]))
    print(result)


if __name__ == "__main__":
    task5()
