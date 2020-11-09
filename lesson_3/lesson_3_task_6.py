# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint

SIZE = 10
MIN_ITEM = -5
MAX_ITEM = 10

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

index_min = 0
index_max = 0

for i in range(len(array)):
    if array[i] > array[index_max]:
        index_max = i
    else:
        if array[i] < array[index_min]:
            index_min = i
s = 0

if index_min < index_max:
    start_index, stop_index = index_min, index_max
else:
    start_index, stop_index = index_max, index_min

for i in range(start_index + 1, stop_index):
    s += array[i]

print(f'Сумма элементов между\nминимальным: "{array[index_min]}"\nи максимальным:'
      f' "{array[index_max]}"\nэлемнатми в массиве\n{array}\nравна: "{s}"' if array else f'Список пуст')
