from lab1.utils import read_file, write_file, checker


def linearfinder(file_in, file_output):
    file_input = read_file(file_in)

    s = [int(i) for i in file_input[0].strip().split()]
    v = int(file_input[1])

    if not(0 <= len(s) <= 10**3):
        write_file(file_output, 'Слишком много элементов')
        exit('Слишком много элементов')

    if abs(v) > 3**10:
        write_file(file_output, 'Число, которое необходимо найти, выходит за ограничение')
        exit('Число, которое необходимо найти, выходит за ограничение')

    if not checker(s, 3):
        write_file(file_output, 'Одно из чисел выходит за ограничение')
        exit('Одно из чисел выходит за ограничение')

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

    write_file(file_output, res_s)