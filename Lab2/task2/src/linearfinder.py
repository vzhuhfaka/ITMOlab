def checker(ar):
    for i in ar:
        if abs(i) > 10**9:
            return False
    return True


file_input = open('input.txt', 'r')
file_output = open('output.txt', 'w+')

s = [int(i) for i in file_input.readline().strip().split()]
v = int(file_input.readline())

if not(0 <= len(s) <= 10**3):
    file_output.write('Too many elements')
    exit('Too many elements')

if not checker(s):
    file_output.write('One of the numbers goes out of bounds')
    exit('One of the numbers goes out of bounds')

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
