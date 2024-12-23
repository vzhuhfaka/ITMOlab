import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
sys.path.insert(0, parent_dir)

from lab4.utils import read_data, write_data


def format_data(commands: list) -> list:
    """
    Форматирует данные под задачу

    Пример:
    ['+ 1', '?', '-', '+ 13'] -> ['1', '?', '-', '13']
    """
    commands_format = []
    for i in commands:
        i_split = i.split()
        if len(i_split) == 2:
            commands_format.append(i_split[1])
        else:
            commands_format.append(i_split[0])
    return commands_format


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
        last_element = self.queue[0]
        self.queue = self.queue[1:]
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
        min_el = 10 ** 10
        # В этом цикле находим наименьшее число в очереди
        for i in range(len(self.queue)):
            el = self.queue_take()
            min_el = min(min_el, int(el))
            self.queue_add(el)

        # В этом цикле берём наименьшее число из очереди
        for i in range(len(self.queue)):
            el = self.queue_take()
            if int(el) == min_el:
                min_el = el
            self.queue_add(el)
        return min_el


def task6():
    PATH_INPUT = 'lab4/task6/txtf/input.txt'
    PATH_OUTPUT = 'lab4/task6/txtf/output.txt'

    commands = read_data(PATH_INPUT)[1:]  # не считаем первую строчку, так как там количество элементов
    commands_format = format_data(commands)

    minimal_elements = []
    queue = Queue([])
    for i in commands_format:
        if i == '?':
            minimal_elements.append(queue.get_min_element())
        elif i == '-':
            queue.queue_take()
        else:
            queue.queue_add(i)

    write_data(PATH_OUTPUT, '\n'.join([i for i in minimal_elements]))
    print(minimal_elements)


if __name__ == "__main__":
    task6()
