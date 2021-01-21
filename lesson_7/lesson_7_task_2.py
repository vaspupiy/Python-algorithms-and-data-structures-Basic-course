# 2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import uniform, random
from collections import deque


def merge(s_arr_1, s_arr_2):
    temp = deque()
    while s_arr_1 and s_arr_2:
        if s_arr_1[-1] > s_arr_2[-1]:
            temp.appendleft(s_arr_1.pop())
        else:
            temp.appendleft(s_arr_2.pop())
    if s_arr_1:
        s_arr_1.extend(temp)
        return s_arr_1
    if s_arr_2:
        s_arr_2.extend(temp)
        return s_arr_2


def float_merge_sort(arr):
    if len(arr) <= 1:
        return
    m = len(arr) // 2
    left_arr = [arr[i] for i in range(0, m)]  # можно и срезами, но очень запуган...
    right_arr = [arr[i] for i in range(m, len(arr))]
    float_merge_sort(left_arr)
    float_merge_sort(right_arr)
    arr[:] = merge(left_arr, right_arr)  # в любом случае переливать полностью один массив в другой... (наверное)
    # return merge(float_merge_sort(arr[:m]), float_merge_sort(arr[m:]))


if __name__ == '__main__':
    SIZE = 10
    N_MIN = -0.0
    N_MAX = 50.0
    # random.uniform(a, b) по некоторым данным, при определенном округлении,
    # может вернуть и b(включительно). Но я таких случаев не зафиксировал :)))
    array = [uniform(N_MIN, N_MAX) for _ in range(SIZE)]

    print('\nИсходный массив :\n', array)
    float_merge_sort(array)
    print('\nОтсортитрованный массив: \n', array)
