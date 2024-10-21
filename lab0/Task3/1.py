import time
t_start = time.perf_counter()

i = open('input.txt', 'r')
o = open('output.txt', 'w+')
n = int(i.readline())
if 0 <= n <= 10 ** 7:
    first_n = 0
    second_n = 1
    for i in range(n - 1):
        first_n, second_n = second_n, first_n + second_n
    o.write(str(second_n % 10))

print(f'время выполнения: {time.perf_counter() - t_start}')