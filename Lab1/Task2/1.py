import time
t_start = time.perf_counter()

i = open('input.txt', 'r')
o = open('output.txt','w+')
n = int(i.readline())
if 0 <= n <= 45:
    a = 0
    b = 1
    for i in range(n-2):
        a, b = b, a + b
    o.write(str(b))
print(f'время выполнения: {time.perf_counter() - t_start}')