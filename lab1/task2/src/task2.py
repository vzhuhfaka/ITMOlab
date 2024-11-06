from lab1.utils import start_collect, write_info, write_in_file


def linearfinder(file_in, file_output, info_file):
    t_start, tracemalloc, file_input = start_collect(file_in)

    s = [int(i) for i in file_input[0].strip().split()]
    v = int(file_input[1])

    res_i = []
    for i in range(len(s)):
        if s[i] == v:
            res_i.append(i)

    res_s = ''
    for i in range(len(res_i)):
        if i == len(res_i) - 1:
            res_s += str(res_i[i])
        else:
            res_s += str(res_i[i]) + ', '

    write_info(info_file, t_start, tracemalloc)
    write_in_file(file_output, res_s)


if __name__ == '__main__':
    linearfinder('../txtf/test_input.txt', '../txtf/test_output.txt', '../txtf/info.txt')