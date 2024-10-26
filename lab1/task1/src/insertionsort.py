from lab1.utils import write_info, start_collect, write_in_file


def insertionsort(file_in, file_out, file_t):
    t_start, tracemalloc, file_input = start_collect(file_in)

    n = int(file_input[0])
    s = [int(el) for el in file_input[1].split()]

    for i in range(1, len(s)):
        value = s[i]
        j = i - 1
        while value < s[j] and j >= 0:
            s[j+1] = s[j]
            j -= 1
        s[j+1] = value

    res_s = ''
    for elem in s:
        res_s += f'{elem} '

    write_info(file_t, t_start, tracemalloc)
    write_in_file(file_out, res_s)
