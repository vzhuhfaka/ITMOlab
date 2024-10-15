def checker(ar):
    for i in ar:
        if abs(i) > 10**3:
            return False
    return True


def linearfinder(file_in, file_out):
    file_input = open(file_in, 'r')
    file_output = open(file_out, 'w+')

    s = [int(i) for i in file_input.readline().strip().split()]
    v = int(file_input.readline())

    if not(0 <= len(s) <= 10**3):
        file_output.write('Слишком много элементов')
        file_output.close()
        exit('Слишком много элементов')

    if abs(v) > 3**10:
        file_output.write('Число, которое необходимо найти, выходит за ограничение')
        file_output.close()
        exit('Число, которое необходимо найти, выходит за ограничение')

    if not checker(s):
        file_output.write('Одно из чисел выходит за ограничение')
        file_output.close()
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

    file_input.close()
    file_output.close()
