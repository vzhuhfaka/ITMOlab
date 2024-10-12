def checker(ar):
    for i in ar:
        if abs(i) > 10**9:
            return False
    return True


file_input = open('input.txt', 'r')
file_output = open('output.txt', 'w+')
n = int(file_input.readline())
s = [int(el) for el in file_input.readline().split()]

if not (1 <= n <= 10**3):
    file_output.write('Wrong first number')
    exit('Wrong first number')

if not checker(s):
    file_output.write('One of the numbers goes out of bounds')
    exit('One of the numbers goes out of bounds')

for i in range(1, len(s)):
    value = s[i]
    j = i - 1
    while value < s[j] and j >= 0:
        s[j+1] = s[j]
        j -= 1
    s[j+1] = value

for elem in s:
    file_output.write(f'{elem} ')

file_input.close()
file_output.close()