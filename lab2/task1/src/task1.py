from lab2.utils import read_lines, write_in_file


def Merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []

    for i in range(n1):
        L.append(A[p + i])
    for j in range(n2):
        R.append(A[q + j + 1])

    i, j = 0, 0
    k = p
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1


def MergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        Merge(A, p, q, r)



if __name__ == '__main__':
    path_input = '../txtf/input.txt'
    path_output = '../txtf/output.txt'

    array = read_lines(path_input)[1] # берём вторую строчку, так как в первой число элементов
    MergeSort(array, 0, len(array)-1)

    write_in_file(path_output, array)
    print(array)
