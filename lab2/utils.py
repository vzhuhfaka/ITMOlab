import time, tracemalloc


def start_collect(input_file):
    t_start = time.perf_counter()
    tracemalloc.start()
    in_f = read_lines(input_file)
    return t_start, tracemalloc, in_f


def write_info(path_info, func, input_data):
    time_start = time.perf_counter()
    tracemalloc.start()

    func(input_data)

    memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    time_ac = time.perf_counter() - time_start
    with open(path_info, 'w+') as f:
        f.write(f'time: {time_ac} s\nmemory: {memory[1] / 2 ** 20} Mb')


def list_to_str(ar):
    res = ''
    for i in ar:
        res += str(i)
    return str(int(res))


def str_to_list(s):
    res = []
    for i in s.split():
        res.append(i)
    return res


def read_lines(file):
    lines = []
    with open(file, 'r') as f:
        for i in f.readlines():
            el = []
            for j in i.strip().split():
                if j != ' ':
                    el.append(int(j))
            lines.append(el)
    return lines

def write_in_file(file, text):
    with open(file, 'w+') as f:
        if isinstance(text, list):
            f.write(str(text)[1:-1])
        elif isinstance(text, str):
            f.write(text)


def read_line(file_txt):
    with open(file_txt, 'r') as f:
        return f.readline()


def txt_to_list(file_txt):
    res = []
    with open(file_txt, 'r') as f:
        for i in f.readline().split():
            res.append(int(i))
    return res