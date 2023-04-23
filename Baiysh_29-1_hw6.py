data = []


def binary_search(list1, n):
    low = 0
    high = 100
    mid = 50
    while True:
        if mid < n:
            data.append(mid)
            low = mid
            mid = (low + high) // 2

        elif mid > n:
            data.append(mid)
            high = mid
            mid = (low + mid) // 2

        elif mid == n:
            data.append(mid)
            return "Программа остоновлена!"


print(binary_search(range(1, 101), 78), f"{data} Количество попыток - {len(data)}")

from random import randint


def bubble(array):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if array[j] > array[j + 1]:
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff


N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))

print(a)
bubble(a)
print(a)
