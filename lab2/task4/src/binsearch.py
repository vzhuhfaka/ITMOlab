import time, tracemalloc
from lab2.utils import read_file, write_file, close_files, write_info


def BinSearch(A, n):
    if len(A) == 0:
        return -1
    if len(A) == 1:
        if A[0] == n:
            return 0
        return -1

    left = 0
    right = len(A) - 1

    while left <= right:
        mid = (left + right) // 2

        if n == A[mid]:
            return mid
        elif n > A[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def search(input_file, output_file, info_file):
    t_start = time.perf_counter()
    tracemalloc.start()

    in_f = read_file(input_file)

    a = in_f[1].strip()
    b = in_f[3].strip()
    result_s = ''
    for i in b.split():
        result_s += str(BinSearch(a.split(), i)) + ' '

    time_ac = time.perf_counter() - t_start
    memory = tracemalloc.get_traced_memory()[1] / 2 ** 20

    write_info(info_file, time_ac, memory)
    write_file(output_file, result_s)

    tracemalloc.stop()
