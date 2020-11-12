# 1). Проанализировать скорость и сложность одного любого алгоритма из разработанных
# в рамках домашнего задания первых трех уроков.

# Выбрал задачу: Определить, какое число в массиве встречается чаще всего.
# На основании проведенных измерений с помощью timeit можно сделать следующие выводы:
# •	функция max_count_elem_1(array_) работает за линейное время
# •	max_count_elem_2(array_) работает за квадратичное время
# •	max_count_elem_3(array_) зависит не только от размера массива, но и от количества уникальных элементов.
# При небольшом количестве уникальных элементов – работает близко к линейному времени,
# при большом разбросе данных – растет квадратично
#
# Анализ алгоритмов с помощью cProfile,
# показал наличие большого количество вызовов  ncalls  для  max_count_elem_2(array)
# вот для такого перехода {built-in method builtins.len},
# сделал предположение, что это вызов len(array_) в цикле,
# но попытка избавится от этого вызова в max_count_elem_2_2(array_) через переменную
# len_arr = len(array_) прироста производительности не дала.
# Видимо скорость  len(array_) не оказывает существенного влияния.


from random import randint
from timeit import timeit
from cProfile import run


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
        else:
            d_elem_count[index] = 1
    return [max_elem_, max_count_]


def max_count_elem_2(array_):
    max_elem_ = array_[0]
    max_count_ = 1
    for i in range(len(array_)):
        count = 1
        for j in range(i + 1, len(array_)):
            if array_[i] == array_[j]:
                count += 1
        if count > max_count_:
            max_count_ = count
            max_elem_ = array[i]
    return [max_elem_, max_count_]


def max_count_elem_2_2(array_):
    max_elem_ = array_[0]
    max_count_ = 1
    len_arr = len(array_)
    for i in range(len_arr):
        count = 1
        for j in range(i + 1, len_arr):
            if array_[i] == array_[j]:
                count += 1
        if count > max_count_:
            max_count_ = count
            max_elem_ = array[i]
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
        if count > max_count_:
            max_elem_ = i
            max_count_ = count
    return [max_elem_, max_count_]


# SIZE = 10
# MIN_ITEM = 0
# MAX_ITEM = 5
# array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(f'Исходный массив: \n{array}')
#
# print(f'Чаще всего в массиве встречается число: \n{max_count_elem_1(array)[0]} '
#       f'\nколичесво повторений: \n{max_count_elem_1(array)[1]}')
# print(f'Чаще всего в массиве встречается число: \n{max_count_elem_2(array)[0]} '
#       f'\nколичесво повторений: \n{max_count_elem_2(array)[1]}')
# print(f'Чаще всего в массиве встречается число: \n{max_count_elem_3(array)[0]} '
#       f'\nколичесво повторений: \n{max_count_elem_3(array)[1]}')

SIZE = 10
MIN_ITEM = -5
MAX_ITEM = 5
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'{"_" * 15} {SIZE=} {MIN_ITEM=} {MAX_ITEM=} {"_" * 15}')
print(timeit('max_count_elem_1(array)', number=1000, globals=globals()))  # 0.0017934000000000005
print(timeit('max_count_elem_2(array)', number=1000, globals=globals()))  # 0.006281200000000001
print(timeit('max_count_elem_2_2(array)', number=1000, globals=globals()))  # 0.005709599999999995
print(timeit('max_count_elem_3(array)', number=1000, globals=globals()))  # 0.0034322000000000033

SIZE = 10
MIN_ITEM = -500
MAX_ITEM = 500
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'{"_" * 15} {SIZE=} {MIN_ITEM=} {MAX_ITEM=} {"_" * 15}')
print(timeit('max_count_elem_1(array)', number=1000, globals=globals()))  # 0.001182499999999996
print(timeit('max_count_elem_2(array)', number=1000, globals=globals()))  # 0.005675300000000001
print(timeit('max_count_elem_2_2(array)', number=1000, globals=globals()))  # 0.005420599999999998
print(timeit('max_count_elem_3(array)', number=1000, globals=globals()))  # 0.0041034

SIZE = 100
MIN_ITEM = -5
MAX_ITEM = 5
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'{"_" * 15} {SIZE=} {MIN_ITEM=} {MAX_ITEM=} {"_" * 15}')
print(timeit('max_count_elem_1(array)', number=1000, globals=globals()))  # 0.0155234
print(timeit('max_count_elem_2(array)', number=1000, globals=globals()))  # 0.34965040000000003
print(timeit('max_count_elem_2_2(array)', number=1000, globals=globals()))  # 0.35556109999999996
print(timeit('max_count_elem_3(array)', number=1000, globals=globals()))  # 0.03239080000000005

SIZE = 100
MIN_ITEM = -500
MAX_ITEM = 500
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'{"_" * 15} {SIZE=} {MIN_ITEM=} {MAX_ITEM=} {"_" * 15}')
print(timeit('max_count_elem_1(array)', number=1000, globals=globals()))  # 0.009876700000000072
print(timeit('max_count_elem_2(array)', number=1000, globals=globals()))  # 0.34749050000000004
print(timeit('max_count_elem_2_2(array)', number=1000, globals=globals()))  # 0.34517090000000006
print(timeit('max_count_elem_3(array)', number=1000, globals=globals()))  # 0.2690633

SIZE = 1000
MIN_ITEM = -5
MAX_ITEM = 5
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'{"_" * 15} {SIZE=} {MIN_ITEM=} {MAX_ITEM=} {"_" * 15}')
print(timeit('max_count_elem_1(array)', number=1000, globals=globals()))  # 0.1523654000000001
print(timeit('max_count_elem_2(array)', number=1000, globals=globals()))  # 37.252773499999996
print(timeit('max_count_elem_2_2(array)', number=1000, globals=globals()))  # 37.6147967
print(timeit('max_count_elem_3(array)', number=1000, globals=globals()))  # 0.30809200000000203

SIZE = 1000
MIN_ITEM = -500
MAX_ITEM = 500
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'{"_" * 15} {SIZE=} {MIN_ITEM=} {MAX_ITEM=} {"_" * 15}')
print(timeit('max_count_elem_1(array)', number=1000, globals=globals()))  # 0.1276088000000044
print(timeit('max_count_elem_2(array)', number=1000, globals=globals()))  # 40.7949093
print(timeit('max_count_elem_2_2(array)', number=1000, globals=globals()))  # 40.082505100000006
print(timeit('max_count_elem_3(array)', number=1000, globals=globals()))  # 17.0061819

SIZE = 10
MIN_ITEM = -5
MAX_ITEM = 5
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'{"_" * 15} {SIZE=} {MIN_ITEM=} {MAX_ITEM=} {"_" * 15}')
run('max_count_elem_1(array)')
#       4 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:8(max_count_elem_1)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

run('max_count_elem_2(array)')
#       15 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:24(max_count_elem_2)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     11    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

run('max_count_elem_2_2(array)')
#       5 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:38(max_count_elem_2_2)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

run('max_count_elem_3(array)')
#       4 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:53(max_count_elem_3)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

SIZE = 10
MIN_ITEM = -500
MAX_ITEM = 500
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'{"_" * 15} {SIZE=} {MIN_ITEM=} {MAX_ITEM=} {"_" * 15}')
run('max_count_elem_1(array)')
#       4 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:8(max_count_elem_1)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

run('max_count_elem_2(array)')
#       15 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:24(max_count_elem_2)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     11    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

run('max_count_elem_2_2(array)')
#       5 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:38(max_count_elem_2_2)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

run('max_count_elem_3(array)')
#       4 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:53(max_count_elem_3)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

SIZE = 100
MIN_ITEM = -5
MAX_ITEM = 5
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'{"_" * 15} {SIZE=} {MIN_ITEM=} {MAX_ITEM=} {"_" * 15}')
run('max_count_elem_1(array)')
#       4 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:8(max_count_elem_1)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
run('max_count_elem_2(array)')
#       105 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:24(max_count_elem_2)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#    101    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

run('max_count_elem_2_2(array)')
#       5 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:38(max_count_elem_2_2)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

run('max_count_elem_3(array)')
#       4 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:53(max_count_elem_3)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

SIZE = 100
MIN_ITEM = -500
MAX_ITEM = 500
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'{"_" * 15} {SIZE=} {MIN_ITEM=} {MAX_ITEM=} {"_" * 15}')
run('max_count_elem_1(array)')
#       4 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:8(max_count_elem_1)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

run('max_count_elem_2(array)')
#       105 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:24(max_count_elem_2)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#    101    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

run('max_count_elem_2_2(array)')
#       5 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:38(max_count_elem_2_2)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

run('max_count_elem_3(array)')
#       4 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:53(max_count_elem_3)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

SIZE = 1000
MIN_ITEM = -5
MAX_ITEM = 5
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'{"_" * 15} {SIZE=} {MIN_ITEM=} {MAX_ITEM=} {"_" * 15}')
run('max_count_elem_1(array)')
#       4 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:8(max_count_elem_1)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

run('max_count_elem_2(array)')
#       1005 function calls in 0.039 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.039    0.039 <string>:1(<module>)
#      1    0.039    0.039    0.039    0.039 Lesson_4_task_1.py:24(max_count_elem_2)
#      1    0.000    0.000    0.039    0.039 {built-in method builtins.exec}
#   1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

run('max_count_elem_2_2(array)')
#       5 function calls in 0.036 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.036    0.036 <string>:1(<module>)
#      1    0.036    0.036    0.036    0.036 Lesson_4_task_1.py:38(max_count_elem_2_2)
#      1    0.000    0.000    0.036    0.036 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
run('max_count_elem_3(array)')
#       4 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:53(max_count_elem_3)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

SIZE = 1000
MIN_ITEM = -500
MAX_ITEM = 500
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'{"_" * 15} {SIZE=} {MIN_ITEM=} {MAX_ITEM=} {"_" * 15}')
run('max_count_elem_1(array)')
#       4 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:8(max_count_elem_1)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
run('max_count_elem_2(array)')
#       1005 function calls in 0.037 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.037    0.037 <string>:1(<module>)
#      1    0.037    0.037    0.037    0.037 Lesson_4_task_1.py:24(max_count_elem_2)
#      1    0.000    0.000    0.037    0.037 {built-in method builtins.exec}
#   1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

run('max_count_elem_2_2(array)')
#       5 function calls in 0.037 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.037    0.037 <string>:1(<module>)
#      1    0.037    0.037    0.037    0.037 Lesson_4_task_1.py:38(max_count_elem_2_2)
#      1    0.000    0.000    0.037    0.037 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

run('max_count_elem_3(array)')
#       4 function calls in 0.017 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.017    0.017 <string>:1(<module>)
#      1    0.017    0.017    0.017    0.017 Lesson_4_task_1.py:53(max_count_elem_3)
#      1    0.000    0.000    0.017    0.017 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
