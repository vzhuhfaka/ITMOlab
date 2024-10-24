from lab2.utils import write_in_file, write_info, start_collect


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
    t_start, tracemalloc, in_f = start_collect(input_file)

    a = in_f[1].strip()
    b = in_f[3].strip()
    result_s = ''
    for i in b.split():
        result_s += str(BinSearch(a.split(), i)) + ' '

    write_info(info_file, t_start, tracemalloc)
    write_in_file(output_file, result_s)
