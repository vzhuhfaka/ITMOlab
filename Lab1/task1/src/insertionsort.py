import time, tracemalloc
from utils import read_file, write_file, close_files


def checker(ar):
    for i in ar:
        if abs(i) > 10**9:
            return False
    return True


def insertionsort(file_in, file_out, file_t):
    t_start = time.perf_counter()
    tracemalloc.start()

    file_info = write_file(file_t)
    file_input = read_file(file_in)
    file_output = write_file(file_out)

    n = int(file_input[0])
    s = [int(el) for el in file_input[1].split()]

    if not (1 <= n <= 10**3):
        file_output.write('Неверное первое число')
        close_files(file_info, file_output)
        exit('Неверное первое число')

    if n != len(s):
        file_output.write('Количество элементов не совпадает с заданным значением')
        close_files(file_info, file_output)
        exit('Количество элементов не совпадает с заданным значением')

    if not checker(s):
        file_output.write('Одно из чисел выходит за ограничение')
        close_files(file_info, file_output)
        exit('Одно из чисел выходит за ограничение')

    for i in range(1, len(s)):
        value = s[i]
        j = i - 1
        while value < s[j] and j >= 0:
            s[j+1] = s[j]
            j -= 1
        s[j+1] = value

    for elem in s:
        file_output.write(f'{elem} ')

    file_info.write(f'time: {time.perf_counter() - t_start} s\nmemory: {tracemalloc.get_traced_memory()[1]/2**20} Mb')
    close_files(file_info, file_output)
