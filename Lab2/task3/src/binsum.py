import time

def list_to_str(ar):
    res = ''
    for i in ar:
        res += str(i)
    return str(int(res))


def str_to_list(s):
    s = str(s)
    res = []
    for i in s:
        res.append(i)
    return res


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

    file_time = open(file_t, 'w+')
    file_input = open(file_in, 'r')
    file_output = open(file_out, 'w+')
    n1, n2 = map(str, file_input.read().split())
    if (not (1 <= int(n1) <= 10 ** 3)) or (not (1 <= int(n2) <= 10 ** 3)):
        file_output.write('One of the numbers goes out of bounds')
        exit('One of the numbers goes out of bounds')

    A, B = str_to_list(n1), str_to_list(n2)

    C = bin_sum(A, B)
    file_output.write(list_to_str(C))

    file_time.write(f'время выполнения: {time.perf_counter() - t_start}')

    file_input.close()
    file_output.close()

