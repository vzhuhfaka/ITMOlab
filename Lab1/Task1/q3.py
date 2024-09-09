inp = open('3/input.txt', 'r')
out = open('3/output.txt', 'w+')
s = inp.readline()
a, b = int(s.split()[0]), int(s.split()[1])
if -10 ** 9 <= a <= 10 ** 9 and -10 ** 9 <= b <= 10 ** 9:
    out.write(str(a+b))
