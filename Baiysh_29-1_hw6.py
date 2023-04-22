from random import randint

N = 10


def selection_sort(row):
    n = len(row)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if row[j] < row[m]:
                m = j
        row[i], row[m] = row[m], row[i]


arr = [randint(1, 99) for item in range(N)]
print(arr)

selection_sort(arr)
print(arr)
