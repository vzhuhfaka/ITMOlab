import time, tracemalloc
from lab2.utils import read_file, write_file, close_files, write_info


def majority_number(A):
    if len(A) == 1:
        return A[0]

    q = len(A) // 2
    left = majority_number(A[:q])
    right = majority_number(A[q:])

    if left == right:
        return left

    left_count = A.count(left)
    right_count = A.count(right)

    if left_count > right_count:
        return left
    else:
        return right


def majority(input_file, output_file, info_file):
    t_start = time.perf_counter()
    tracemalloc.start()

    in_f = read_file(input_file)

    ar = in_f[1].split()

    if ar.count(majority_number(ar)) > len(ar) / 2:
        write_file(output_file, '1')
    else:
        write_file(output_file, '0')

    time_ac = time.perf_counter() - t_start
    memory = tracemalloc.get_traced_memory()[1] / 2 ** 20

    write_info(info_file, time_ac, memory)
    tracemalloc.stop()
