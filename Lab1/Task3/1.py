import time
t_start = time.perf_counter()

i = open('input.txt', 'r')
o = open('output.txt', 'w+')
n = int(i.readline())
if 0 <= n <= 10 ** 7:
    a = 0
    b = 1
    for i in range(n - 1):
        a, b = b, a + b
    o.write(str(b % 10))

print(f'время выполнения: {time.perf_counter() - t_start}')