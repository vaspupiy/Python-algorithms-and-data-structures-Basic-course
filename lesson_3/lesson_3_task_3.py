# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

min_index, max_index = 0, 0  # Присваиваем индекскам минимального и максимального числа значения 0

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

# array = [0, 59, 5, 94, 39, 20, 15, 86, 83, 95]  # проверка для крайних элементов
# array = [0, 59, 5, 0, 39, 20, 95, 86, 83, 95]  # проверка для задвоенных элементов

print(f'Исходный массив: \n{array}')
for i in range(1, len(array)):
    if array[i] > array[max_index]:
        max_index = i
    else:
        if array[i] < array[min_index]:
            min_index = i
array[min_index], array[max_index] = array[max_index], array[min_index]
print(f'Итоговый массив: \n{array}')
