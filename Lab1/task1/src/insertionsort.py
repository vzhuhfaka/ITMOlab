import time, tracemalloc


def checker(ar):
    for i in ar:
        if abs(i) > 10**9:
            return False
    return True


def insertionsort(file_in, file_out, file_t):
    t_start = time.perf_counter()
    tracemalloc.start()

    file_info = open(file_t, 'w+')
    file_input = open(file_in, 'r')
    file_output = open(file_out, 'w+')

    n = int(file_input.readline())
    s = [int(el) for el in file_input.readline().split()]

    if not (1 <= n <= 10**3):
        file_output.write('Неверное первое число')
        file_output.close()
        exit('Неверное первое число')

    if n != len(s):
        file_output.write('Количество элементов не совпадает с заданным значением')
        file_output.close()
        exit('Количество элементов не совпадает с заданным значением')

    if not checker(s):
        file_output.write('Одно из чисел выходит за ограничение')
        file_output.close()
        exit('Одно из чисел выходит за ограничение')

    for i in range(1, len(s)):
        value = s[i]
        j = i - 1
        while value < s[j] and j >= 0:
            s[j+1] = s[j]
            j -= 1
        s[j+1] = value

    for elem in s:
        file_output.write(f'{elem} ')

    file_info.write(f'время выполнения: {time.perf_counter() - t_start} с\nзатраченная память: {tracemalloc.get_traced_memory()[1]/2**20} Мб')

    file_input.close()
    file_output.close()