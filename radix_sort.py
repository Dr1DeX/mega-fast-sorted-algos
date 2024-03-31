import timeit
import random


def comparator_counting(arr, exp_bit):
    n = len(arr)

    out = [0] * n

    count = [0] * 10

    for i in range(0, n):
        idx = arr[i] // exp_bit
        count[idx % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        idx = arr[i] // exp_bit
        out[count[idx % 10] - 1] = arr[i]
        count[idx % 10] -= 1
        i -= 1
    for i in range(0, len(arr)):
        arr[i] = out[i]


def radix_sort(arr):
    max_num = max(arr)
    exp_bit = 1
    while max_num / exp_bit >= 1:
        comparator_counting(arr, exp_bit)
        exp_bit *= 10


arr = [random.randint(0, 100000) for _ in range(0, 10000000)]
start_time = timeit.default_timer()
radix_sort(arr)
print(f'Время работы программы: radix_sort = {timeit.default_timer() - start_time}')

