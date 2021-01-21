# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint

SIZE = 15
MIN_ITEM = 0
MAX_ITEM = 5

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: \n{array}')

max_elem = array[0] if array else None
max_count = 1 if array else None
d_elem_count = {}

for i in array:
    if i in d_elem_count:
        d_elem_count[i] += 1
        if d_elem_count[i] > max_count:
            max_elem = i
            max_count = d_elem_count[i]
    else:
        d_elem_count[i] = 1

print(f'Чаще всего в массиве встречается число: \n{max_elem} \nколичесво повторений: \n{max_count}')
