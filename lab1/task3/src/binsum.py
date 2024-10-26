from lab1.utils import write_in_file, str_to_list, write_info, start_collect, list_to_str


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


def main_binsum(file_in, file_output, info_file):
    t_start, tracemalloc_s, file_input = start_collect(file_in)

    n1, n2 = map(str, file_input[0].split())

    A, B = str_to_list(n1), str_to_list(n2)

    C = bin_sum(A, B)

    write_info(info_file, t_start, tracemalloc_s)
    write_in_file(file_output, list_to_str(C))
