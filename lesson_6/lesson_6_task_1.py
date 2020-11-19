# 1. Подсчитать, сколько было выделено памяти под переменные
# в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с
# наиболее эффективным использованием памяти.

# Выбрал задачу: Определить, какое число в массиве встречается чаще всего.

# Использую Python 3.8.4rc1 (tags/v3.8.4rc1:6c38841, Jun 30 2020, 15:17:30) [MSC v.1924 64 bit (AMD64)] on win32

# Проведенные тесты показали, что наиболее затратные по памяти являются 1 и 3 реализации,
# в зависимости уникалности данных списка, объем использумой памяти может меняться как для 1-й так и для 3-й реализации.
# Объем использумой памяти для 2-й реализации зависит от размера массива. От содержимого массива почти не завист
# ( почти, по тому что тип данных int, и 0 весит меньше чем 100)
#
# _______________ SIZE=10 MIN_ITEM=-100 MAX_ITEM=100 _______________
# Исходный массив:
# [-39, -41, 26, -9, -31, 19, 22, -18, 57, -12]
# Первая реалзация: 1468
# Вторая реалзация: 604
# Третья реалзация: 1612
# _______________ SIZE=10 MIN_ITEM=-3 MAX_ITEM=3 _______________
# Исходный массив:
# [-2, 2, 3, 3, -2, 2, 3, -2, -1, 2]
# Первая реалзация: 1004
# Вторая реалзация: 604
# Третья реалзация: 932
# _______________ SIZE=50 MIN_ITEM=-100 MAX_ITEM=100 _______________
# Исходный массив:
# [24, -3, 3, 95, -7, 20, -76, -37, -68, -2, -82, -34, 54, 95, 94, -68, 33, -23, 91, 41, 3, 41, -45, 7, -44, -65, -3,
# -13, -18, 69, -43, 22, 16, 87, -60, 29, 32, -72, 13, -14, 64, 89, -14, 39, 39, 79, 44, 64, 71, -36]
# Первая реалзация: 5532
# Вторая реалзация: 2060
# Третья реалзация: 5500
# _______________ SIZE=50 MIN_ITEM=-1 MAX_ITEM=1 _______________
# Исходный массив:
# [-1, 1, 1, 1, 1, 0, -1, 1, -1, 1, -1, 0, -1, -1, 1, 0, -1, -1, -1, 1, -1, -1, 0, 0, -1, -1, 1, 1, 1, -1, 0, -1, 0,
# 1, -1, 0, -1, 1, -1, 0, -1, 0, 1, 0, -1, 0, -1, 0, 0, 1]
# Первая реалзация: 2344
# Вторая реалзация: 2004
# Третья реалзация: 2300
# _______________ SIZE=100 MIN_ITEM=-100 MAX_ITEM=100 _______________
# Исходный массив:
# [20, 61, 41, -84, -3, -90, -17, 2, 26, -33, 10, 74, 15, 28, -86, 51, 2, 83, 24, 76, 11, -81, 86, 74, -77, -67, -84,
# -81, -98, -7, -88, 82, -46, 9, 64, -62, 39, 80, -35, -37, -46, -88, -5, 21, -95, -54, -71, -43, 24, -68, 91, -86,
# -76, -48, 53, -54, -40, 5, -90, 17, 57, -92, -95, 88, 20, 34, -90, -30, 56, -16, -54, 89, 58, 91, -69, 80, -6, 48,
# -52, -24, 12, 97, -96, -46, -83, 98, -15, -56, -82, -68, -15, -49, -33, -72, -71, 35, -98, -45, -27, 95]
# Первая реалзация: 10428
# Вторая реалзация: 3844
# Третья реалзация: 14436
#
# Process finished with exit code 0


import sys
from random import randint


def sum_bit(*args):
    """ Вычисляет суммарный объем памяти в байтах, который занимают переданные на вход переменные"""
    s = 0
    for i in args:
        s += sys.getsizeof(i)
        if hasattr(i, '__iter__'):
            if hasattr(i, 'items'):
                for key, val in i.items():
                    s += sys.getsizeof(key)
                    s += sys.getsizeof(val)
            elif not isinstance(i, str):
                for elem in i:
                    s += sys.getsizeof(elem)
    log.append(s)  # расчитываю получить... эмм... разъяснения, на сколько допустимо так делать...
    return


def max_count_elem_1(array_):
    max_elem_ = array_[0] if array_ else None
    max_count_ = 1 if array_ else None
    d_elem_count = {}

    for index in array_:
        if index in d_elem_count:
            d_elem_count[index] += 1
            if d_elem_count[index] > max_count_:
                max_elem_ = index
                max_count_ = d_elem_count[index]
            sum_bit(d_elem_count, max_elem_, max_count_, index, array_, )  # устанавливаю в те места, где считаю
        else:
            d_elem_count[index] = 1
        sum_bit(d_elem_count, max_elem_, max_count_, index, array_, )  # целесообразным провести замеры
    sum_bit(d_elem_count, max_elem_, max_count_, array_, )
    return [max_elem_, max_count_]


def max_count_elem_2(array_):
    max_elem_ = array_[0]
    max_count_ = 1
    for i in range(len(array_)):
        count = 1
        for j in range(i + 1, len(array_)):
            if array_[i] == array_[j]:
                count += 1
            sum_bit(max_elem_, max_count_, i, j, count, array_, )  
        if count > max_count_:
            max_count_ = count
            max_elem_ = array[i]
            sum_bit(max_elem_, max_count_, i, count, array_, )
    sum_bit(max_elem_, max_count_, array_, )
    return [max_elem_, max_count_]


def max_count_elem_3(array_):
    check_set = set(array_)
    max_elem_ = array_[0]
    max_count_ = 1
    for i in check_set:
        count = 0
        for j in array_:
            if i == j:
                count += 1
            sum_bit(check_set, max_elem_, max_count_, i, j, count, array_)
        if count > max_count_:
            max_elem_ = i
            max_count_ = count
        sum_bit(check_set, max_elem_, max_count_, i, count, array_)
    sum_bit(check_set, max_elem_, max_count_, array_)
    return [max_elem_, max_count_]


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100

print(f'{"_" * 15} {SIZE=} {MIN_ITEM=} {MAX_ITEM=} {"_" * 15}')

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: \n{array}')

log = []
max_count_elem_1(array)
print(f'Первая реалзация: {max(log)}')

log = []
max_count_elem_2(array)
print(f'Вторая реалзация: {max(log)}')

log = []
max_count_elem_3(array)
print(f'Третья реалзация: {max(log)}')

SIZE = 10
MIN_ITEM = -3
MAX_ITEM = 3

print(f'{"_" * 15} {SIZE=} {MIN_ITEM=} {MAX_ITEM=} {"_" * 15}')

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: \n{array}')

log = []
max_count_elem_1(array)
print(f'Первая реалзация: {max(log)}')

log = []
max_count_elem_2(array)
print(f'Вторая реалзация: {max(log)}')

log = []
max_count_elem_3(array)
print(f'Третья реалзация: {max(log)}')

SIZE = 50
MIN_ITEM = -100
MAX_ITEM = 100

print(f'{"_" * 15} {SIZE=} {MIN_ITEM=} {MAX_ITEM=} {"_" * 15}')

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: \n{array}')

log = []
max_count_elem_1(array)
print(f'Первая реалзация: {max(log)}')

log = []
max_count_elem_2(array)
print(f'Вторая реалзация: {max(log)}')

log = []
max_count_elem_3(array)
print(f'Третья реалзация: {max(log)}')

SIZE = 50
MIN_ITEM = -1
MAX_ITEM = 1

print(f'{"_" * 15} {SIZE=} {MIN_ITEM=} {MAX_ITEM=} {"_" * 15}')

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: \n{array}')

log = []
max_count_elem_1(array)
print(f'Первая реалзация: {max(log)}')

log = []
max_count_elem_2(array)
print(f'Вторая реалзация: {max(log)}')

log = []
max_count_elem_3(array)
print(f'Третья реалзация: {max(log)}')

SIZE = 100
MIN_ITEM = -100
MAX_ITEM = 100

print(f'{"_" * 15} {SIZE=} {MIN_ITEM=} {MAX_ITEM=} {"_" * 15}')

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: \n{array}')

log = []
max_count_elem_1(array)
print(f'Первая реалзация: {max(log)}')

log = []
max_count_elem_2(array)
print(f'Вторая реалзация: {max(log)}')

log = []
max_count_elem_3(array)
print(f'Третья реалзация: {max(log)}')
