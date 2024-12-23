import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
sys.path.insert(0, parent_dir)

from lab5.utils import read_data, write_data


def data_format(data):
    """
    Форматирует данные под задачу

    Пример: ['A 1', 'A 5', 'X', 'D 2 4'] -> ['A 1', 'A 4', 'X']
    """
    data_ = []
    for i in data:
        i = i.split()
        if i[0] == 'A':
            data_.append(f'A {i[1]}')
        elif i[0] == 'D':
            data_[int(i[1]) - 1] = f'A {i[2]}'
        elif i[0] == 'X':
            data_.append('X')
    return data_



class Queue:
    def __init__(self, queue: list):
        self.queue = queue

    def get_queue(self):
        """
        Возвращает очередь
        """
        return self.queue

    def queue_take(self):
        """
        Берёт элемент из очереди, при этом удаляя его

        Пример: [1, 2, 3] -> 3 и [1, 2]
        """
        last_element = self.queue[-1]
        self.queue = self.queue[:-1]
        return last_element

    def queue_add(self, number):
        """
        Добавляет элемент в очередь
        """
        self.queue.append(number)

    def get_min_element(self):
        """
        Возвращает минимальный элемент из очереди
        """
        min_el = 10**10
        # В этом цикле находим наименьшее число в очереди
        for i in range(len(self.queue)):
            el = self.queue_take()
            min_el = min(min_el, int(el))
            self.queue_add(el)

        # В этом цикле берём наименьшее число из очереди
        for i in range(len(self.queue)):
            el = self.queue_take()
            if int(el) == min_el:
                return el


def main(commands_raw):
    """
    Главная функция, которая выполняет задачу, получает данные, форматирует и возвращает ответ

    Пример: ['A 1', 'A 5', 'X', 'D 2 4', 'X'] -> ['1', '4']
    """
    commands = data_format(commands_raw)
    queue = Queue([])
    minimal_elements = []
    for i in commands:
        i = i.split()
        if i[0] == 'A':
            queue.queue_add(i[1])
        else:
            min_el = queue.get_min_element()
            if min_el:
                minimal_elements.append(min_el)
            else:
                minimal_elements.append('*')
    return minimal_elements


def task3():
    PATH_INPUT = 'lab5/task6/txtf/input.txt'
    PATH_OUTPUT = 'lab5/task6/txtf/output.txt'

    commands = read_data(PATH_INPUT)[1:]
    result = main(commands)

    write_data(PATH_OUTPUT, '\n'.join([i for i in result]))
    print(result)


if __name__ == "__main__":
    task3()
