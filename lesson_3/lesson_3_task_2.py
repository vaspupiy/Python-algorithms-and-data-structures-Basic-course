# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

from random import randint

SIZE = 15
MIN_ITEM = 0
MAX_ITEM = 100

array_1 = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array_2 = []
for i, item in enumerate(array_1):
    if item % 2 == 0:
        array_2.append(i)
print(array_1, array_2, sep='\n')
