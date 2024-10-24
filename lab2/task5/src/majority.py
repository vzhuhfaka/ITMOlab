from lab2.utils import write_in_file, write_info, start_collect


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
    t_start, tracemalloc, in_f = start_collect(input_file)

    ar = in_f[1].split()

    if ar.count(majority_number(ar)) > len(ar) / 2:
        write_in_file(output_file, '1')
    else:
        write_in_file(output_file, '0')

    write_info(info_file, t_start, tracemalloc)
