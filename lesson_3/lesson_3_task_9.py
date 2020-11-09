# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint


def show_matrix(matrix_):
    """Вывдит на экран матрицу самым красавенным образом"""
    for row in matrix:
        for elem in row:
            print(f'{elem:>4}', end='')
        print()
    print()


COUNT_LINE = 5
COUNT_COLUMN = 3
MIN_ITEM = -5
MAX_ITEM = 5
OFFSET = 4

matrix = [[randint(MIN_ITEM, MAX_ITEM) for _ in range(COUNT_COLUMN)] for _ in range(COUNT_LINE)]

# print('Матрица до вычислений:')
# show_matrix(matrix)

min_item_arr = [i for i in matrix[0]]

#  находим минимальные элементы столбцов
for line in matrix:
    for i, item in enumerate(line):
        if min_item_arr[i] > item:
            min_item_arr[i] = item

#  находим максимальный элемент среди...
max_num = min_item_arr[0]
for item in min_item_arr[1:]:
    if item > max_num:
        max_num = item

print('Матрица после вычислений:')
show_matrix(matrix)

# print('Минимальные элементы столбцов матрицы: ')
# for item in min_item_arr:
#     print(f'{item:>4}', end='')
# print()
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: \n{max_num:>4}')
