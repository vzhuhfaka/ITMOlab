from lab6.utils import read_data, write_data

class Set:
    """
    Класс множества
    """
    def __init__(self, _set):
        self._set = _set

    def hash_function(self, obj):
        """
        Хэш функция, которая считает сумму цифр и возвращает остаток от деления на размер хеш-таблицы
        """
        return sum([int(i) for i in obj]) % len(self._set)

    def add(self, number):
        """
        Добавляет элемент в хеш-таблицу
        """
        name_id = self.hash_function(number)
        if [name_id, number] not in self._set[name_id]:
            self._set[name_id].append([name_id, number])

    def del_(self, number):
        """
        Удаляет элемент из хеш-таблицы
        """
        name_id = self.hash_function(number)
        for i in self._set[name_id]:
            if i[1] == number:
                self._set[name_id].remove(i)
                break

    def find_(self, number):
        """
        Ищет элемент в хеш-таблице
        """
        name_id = self.hash_function(number)
        for i in self._set[name_id]:
            if i[1] == number:
                return 'Y'
        return 'N'


def main(data):
    """
    Функция для решения задачи, которая работает с хеш-таблицей

    Пример входных данных: [['add', '123', 'John'], ['del', '22'], ['find', '434']]
    Пример выходных данных: ['John', 'not found', 'not found']
    """
    book = [[] for _ in range(10)]
    result = []
    phone_book = Set(book)
    for i in data:
        if i[0] == 'A':
            phone_book.add(number=i[1])
        elif i[0] == 'D':
            phone_book.del_(number=i[1])
        elif i[0] == '?':
            result.append(phone_book.find_(number=i[1]))
    return result


def task1():
    PATH_INPUT = '../txtf/input.txt'
    PATH_OUTPUT = '../txtf/output.txt'

    data_split = [i.strip().split() for i in read_data(PATH_INPUT)[1:]]

    result = main(data_split)

    write_data(PATH_OUTPUT, '\n'.join(result))
    print(result)


if __name__ == "__main__":
    task1()
