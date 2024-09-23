import time
t_start = time.perf_counter()

i = open('input.txt', 'r')
o = open('output.txt','w+')
n = int(i.readline())
first_n = 0
second_n = 1
if 0 <= n <= 45:
    for i in range(n-1):
        first_n, second_n = second_n, first_n + second_n
    o.write(str(second_n))
print(f'время выполнения: {time.perf_counter() - t_start}')