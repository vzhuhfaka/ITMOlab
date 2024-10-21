from utils import read_file, write_file, close_files


def checker(ar):
    for i in ar:
        if abs(i) > 10**3:
            return False
    return True


def linearfinder(file_in, file_out):
    file_input = read_file(file_in)
    file_output = write_file(file_out)

    s = [int(i) for i in file_input[0].strip().split()]
    v = int(file_input[1])

    if not(0 <= len(s) <= 10**3):
        file_output.write('Слишком много элементов')
        close_files(file_output)
        exit('Слишком много элементов')

    if abs(v) > 3**10:
        file_output.write('Число, которое необходимо найти, выходит за ограничение')
        close_files(file_output)
        exit('Число, которое необходимо найти, выходит за ограничение')

    if not checker(s):
        file_output.write('Одно из чисел выходит за ограничение')
        close_files(file_output)
        exit('Одно из чисел выходит за ограничение')

    res_i = []
    for i in range(len(s)):
        if s[i] == v:
            res_i.append(i)

    for i in range(len(res_i)):
        if i == len(res_i) - 1:
            file_output.write(str(res_i[i]))
        else:
            file_output.write(str(res_i[i]) + ', ')

    close_files(file_output)