import time
from utils import read_file,write_file, close_files, str_to_list, list_to_str


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


def main_binsum(file_in, file_out, file_t):
    t_start = time.perf_counter()

    file_time = write_file(file_t)
    file_input = read_file(file_in)
    file_output = write_file(file_out)

    n1, n2 = map(str, file_input[0].split())
    if (not (1 <= len(n1) <= 10 ** 3)) or (not (1 <= len(n2) <= 10 ** 3)):
        file_output.write('Одно из чисел выходит за ограничение')
        close_files(file_time, file_output)
        exit('Одно из чисел выходит за ограничение')

    A, B = str_to_list(n1), str_to_list(n2)

    C = bin_sum(A, B)
    file_output.write(list_to_str(C))

    file_time.write(f'time: {time.perf_counter() - t_start}')

    close_files(file_time, file_output)