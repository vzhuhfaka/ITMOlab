s = input()
a, b = int(s.split()[0]), int(s.split()[1])
if -10**9 <= a <= 10**9 and -10**9 <= b <= 10**9:
    print(a + b)
else:
    print('неверные числа')