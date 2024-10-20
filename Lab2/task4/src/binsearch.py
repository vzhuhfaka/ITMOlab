import time, tracemalloc


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

    in_f = open(input_file, 'r').readlines()
    out_f = open(output_file, 'w+')
    info_f = open(info_file, 'w+')

    a = in_f[1].strip()
    b = in_f[3].strip()
    result_s = ''
    for i in b.split():
        result_s += str(BinSearch(a.split(), i)) + ' '
    out_f.write(result_s)

    info_f.write(f'time: {time.perf_counter() - t_start} s\nmemory: {tracemalloc.get_traced_memory()[1] / 2 ** 20} Mb')

    tracemalloc.stop()
    info_f.close()
    out_f.close()
