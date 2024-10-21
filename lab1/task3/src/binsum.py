import time, tracemalloc
from lab1.utils import read_file, write_file, str_to_list, list_to_str, write_info


def bin_sum(A, B):
    C = []
    t = 0
    A.reverse()
    B.reverse()
    for i in range(len(A)):
        a = int(A[i])
        b = int(B[i])
        c = a + b + t
        C.append(c % 2)
        t = c // 2
    C.append(t)
    return C[::-1]


def main_binsum(file_in, file_out, file_info):
    t_start = time.perf_counter()
    tracemalloc.start()

    file_input = read_file(file_in)

    n1, n2 = map(str, file_input[0].split())
    if (not (1 <= len(n1) <= 10 ** 3)) or (not (1 <= len(n2) <= 10 ** 3)):
        write_file(file_out, 'Одно из чисел выходит за ограничение')
        exit('Одно из чисел выходит за ограничение')

    A, B = str_to_list(n1), str_to_list(n2)

    C = bin_sum(A, B)

    time_ac = time.perf_counter() - t_start
    memory = tracemalloc.get_traced_memory()[1] / 2 ** 20

    write_info(file_info, time_ac, memory)
    write_file(file_out, list_to_str(C))
