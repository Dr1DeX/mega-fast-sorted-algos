import timeit
import random
from radix_sort import radix_sort
from merge_sort import merge_sort


def timer_radix_sort():
    arr = [random.randint(0, 10000000) for _ in range(0, 10000000)]
    print('Func radix_sort executor to start')
    radix_sort(arr)
    print('Func radix_sort complete:')


def timer_merge_sort():
    arr = [random.randint(0, 10000000) for _ in range(0, 10000000)]
    print('Func merge_sort executor to start')
    merge_sort(arr)
    print('Func merge_sort complete:')


start_time = timeit.default_timer()
timer_radix_sort()
print(timeit.default_timer() - start_time)
start_time = timeit.default_timer()
timer_merge_sort()
print(timeit.default_timer() - start_time)