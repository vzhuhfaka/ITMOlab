import time, tracemalloc
from lab1.utils import read_file, write_file, write_info, checker


def insertionsort(file_in, file_out, file_t):
    t_start = time.perf_counter()
    tracemalloc.start()

    file_input = read_file(file_in)

    n = int(file_input[0])
    s = [int(el) for el in file_input[1].split()]

    if not (1 <= n <= 10**3):
        write_file(file_out, 'Неверное первое число')
        exit('Неверное первое число')

    if n != len(s):
        write_file(file_out, 'Количество элементов не совпадает с заданным значением')
        exit('Количество элементов не совпадает с заданным значением')

    if not checker(s, 9):
        write_file(file_out, 'Одно из чисел выходит за ограничение')
        exit('Одно из чисел выходит за ограничение')

    for i in range(1, len(s)):
        value = s[i]
        j = i - 1
        while value < s[j] and j >= 0:
            s[j+1] = s[j]
            j -= 1
        s[j+1] = value

    res_s = ''
    for elem in s:
        res_s += f'{elem} '

    write_file(file_out, res_s)

    time_ac = time.perf_counter() - t_start
    memory = tracemalloc.get_traced_memory()[1] / 2 ** 20

    write_info(file_t, time_ac, memory)
