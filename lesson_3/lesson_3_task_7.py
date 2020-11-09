# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import randint

SIZE = 20
MIN_ITEM = -1
MAX_ITEM = 15

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
min_array = [array[0], array[1]] if array[0] < array[1] else [array[1], array[0]]  # надеюсь так можно сортировать :)
#  можно создать перменные m1, m2 и в m1 хранить самое маленькое а в m2 второе наименьшее (либо = m1)

for i in array[2:]:
    if i < min_array[1]:  # i < m2
        min_array[1] = i  # m2 = i
        if min_array[1] < min_array[0]:  # m2 < m1
            min_array[0], min_array[1] = min_array[1], min_array[0]  # m1, m2 = m2, m1

print(array)
print(*min_array)  # print(m1, m2)
