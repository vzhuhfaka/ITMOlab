from lab5.utils import read_data, write_data


def min_heap(array, len_ar):
    """
    Возвращает индексы перестановок для пирамиды min-heap

    Пример: [5, 4, 3, 2, 1] -> [(0, 4), (1, 4), (2, 4), (3, 4)]
    """
    perms = []
    c = 0
    for i in range(1, len_ar):
        perm_i = i - 1
        perm_j = array.index(min(array[i:]))
        if array[i - 1] > array[perm_j]:
            array[perm_i], array[perm_j] = array[perm_j], array[perm_i]
            perms.append((perm_i, perm_j))
            c += 1
    return [perms, c]


def task1():
    PATH_INPUT = '../txtf/input.txt'
    PATH_OUTPUT = '../txtf/output.txt'

    data = read_data(PATH_INPUT)
    array_ = [int(i) for i in data[1].split(' ')]
    n = int(data[0])
    result = min_heap(array_, n)

    # Записывает результат в файл, используя форматирование
    # Пример: [[(0, 4), (1, 3)], 2] -> '2\n 0 4\n 1 3'
    write_data(PATH_OUTPUT, f'{result[1]}\n' + '\n'.join([str(key) + ' ' + str(value) for key, value in result[0]]))
    print(result)


if __name__ == "__main__":
    task1()
