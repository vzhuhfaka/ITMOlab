import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
sys.path.insert(0, parent_dir)

from lab6.utils import read_data, write_data

class PhoneBook:
    """
    Класс для телефонной книги, использующий хеш-таблицу для хранения данных
    """
    def __init__(self, book):
        self.book = book

    def hash_function(self, obj):
        """
        Хэш функция, которая считает сумму цифр и возвращает остаток от деления на размер хеш-таблицы
        """
        return sum([int(i) for i in obj]) % len(self.book)

    def add(self, number, name):
        """
        Добавляет запись в хеш-таблицу
        """
        name_id = self.hash_function(number)
        self.book[name_id] = [name, number]

    def del_(self, number):
        """
        Удаляет запись в хеш-таблице
        """
        name_id = self.hash_function(number)
        self.book[name_id] = ['', '']

    def find_(self, number):
        """
        Ищет запись в хеш-таблице
        """
        name_id = self.hash_function(number)
        if self.book[name_id] != ['', '']:
            return self.book[name_id][0]
        else:
            return 'not found'


def main(data):
    """
    Функция для решения задачи, которая работает с хеш-таблицей

    Пример входных данных: [['add', '123', 'John'], ['del', '22'], ['find', '434']]
    Пример выходных данных: ['John', 'not found', 'not found']
    """
    book = [['', ''] for i in range(10)]
    result = []
    phone_book = PhoneBook(book)
    for i in data:
        if i[0] == 'add':
            phone_book.add(number=i[1], name=i[2])
        elif i[0] == 'del':
            phone_book.del_(number=i[1])
        elif i[0] == 'find':
            result.append(phone_book.find_(number=i[1]))
    return result


def task2():
    PATH_INPUT = 'lab6/task2/txtf/input.txt'
    PATH_OUTPUT = 'lab6/task2/txtf/output.txt'

    data_split = [i.strip().split() for i in read_data(PATH_INPUT)[1:]]

    result = main(data_split)

    write_data(PATH_OUTPUT, '\n'.join(result))
    print(result)


if __name__ == "__main__":
    task2()
