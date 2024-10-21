def read_input(input_file):
    with open(input_file, 'r') as f:
        return f.readlines()


def write_info(info_file):
    with open(info_file, 'w+') as f:
        return f


def write_output(output_file):
    with open(output_file, 'w+') as f:
        return f


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