import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
sys.path.insert(0, parent_dir)

from lab4.utils import read_data, write_data


def get_stack_deletions(commands: list) -> list:
    """
    Возвращает список удалённых элементов в стеке

    Пример:
    ['10', '-', '3', '1', '-'] -> ['10', '1']
    """
    stack = []
    deleted_elements = []
    for i in commands:
        if i != '-':
            stack.append(i)
        else:
            deleted_elements.append(stack[-1])
            stack = stack[:-1]
    return deleted_elements


def format_input(commands: list) -> list:
    """
    Форматирует входные данные

    Пример:
    ['+ 1', '+ 10', '-', '+2', '+ 1234', '-'] -> ['1', '10', '-', '2', '1234', '-']
    """
    commands_format = []
    for i in commands:
        i_split = i.split()
        if len(i_split) == 2:
            commands_format.append(i_split[1])
        else:
            commands_format.append(i_split[0])
    return commands_format


def task1():
    path_input = 'lab4/task1/txtf/input.txt'
    path_output = 'lab4/task1/txtf/output.txt'

    origin_input = read_data(path_input)

    commands = read_data(path_input)[1:]  # не считаем первую строчку, так как там количество элементов
    commands_format = format_input(commands)
    deleted_elements = get_stack_deletions(commands_format)
    deleted_elements_str = ', '.join(deleted_elements)  # преобразуем список в строку

    write_data(path_output, deleted_elements_str)
    print(origin_input)
    print(deleted_elements)


if __name__ == "__main__":
    task1()
