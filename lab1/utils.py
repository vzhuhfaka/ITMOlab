import time, tracemalloc


def start_collect(input_file):
    t_start = time.perf_counter()
    tracemalloc.start()
    in_f = read_file(input_file)
    return t_start, tracemalloc, in_f


def write_info(file, t_start, tracemalloc):
    with open(file, 'w+') as f:
        time_ac = time.perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 2 ** 20
        f.write(f'time: {time_ac} s\nmemory: {memory} Mb')
        tracemalloc.stop()


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


def read_file(file):
    with open(file, 'r') as f:
        return f.readlines()


def write_in_file(file, text):
    with open(file, 'w+') as f:
        f.write(text)


def txt_to_str(file_txt):
    with open(file_txt, 'r') as f:
        return f.readline()


def txt_to_numlist(file_txt):
    res = []
    with open(file_txt, 'r') as f:
        for i in f.readline():
            if i in '0123456789':
                res.append(i)
    return res


def txt_to_list(file_txt):
    res = []
    with open(file_txt, 'r') as f:
        for i in f.readline().split():
            res.append(int(i))
    return res