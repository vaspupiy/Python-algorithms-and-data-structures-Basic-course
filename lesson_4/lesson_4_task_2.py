# 2). Написать два алгоритма нахождения i-го по счёту простого числа.
#     Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
#     Проанализировать скорость и сложность алгоритмов.
#
# На основании проведенных измерений с помощью timeit можно сделать следующие выводы:
# •	функция eratosthenes(n_, magic_number=15) работает практически за линейное время
# •	prime_num_brut(n_) работает явно хуже чем n**2,
# возможно на больших входных данных можно было бы увидеть и хуже чем n**3,
# но завтра рано на работу вставать(т.е. уже сегодня)…

# cProfile не выявил у prime_num_brut(n_) слабых мест
# У def eratosthenes(n_, magic_number=15) :
#     1335    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# замена sieve_.append(sieve[i]) в цикле на sieve_ = [i for i in sieve if i != 0], после цикла
# видимого прироста производительности не дает (на тесте timeit)


from timeit import timeit
from cProfile import run


def prime_num_brut(n_):
    n_i = 1
    pr_num = 2
    num = 2
    while n_i < n_:
        num += 1
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            pr_num = num
            n_i += 1
    return pr_num


def eratosthenes(n_, magic_number=15):
    sieve = [i for i in range(n_ * magic_number)]

    sieve[1] = 0
    sieve_ = []
    for i in range(2, n_ * magic_number):
        if sieve[i] != 0:
            sieve_.append(sieve[i])
            j = i + i
            while j < n_ * magic_number:
                sieve[j] = 0
                j += i
    # sieve_ = [i for i in sieve if i != 0]
    if len(sieve_) >= n_:
        return sieve_[n_ - 1]
    return f'Не срослось :(  - слишком большое n... поробуйте увеличить magic_number на 1'


MAGIC_NUMBER = 11  # подкручивает исходный размер массива для Эратосфена относительно n
N = 4
print(prime_num_brut(N))
print(eratosthenes(N, MAGIC_NUMBER))

MAGIC_NUMBER = 11  # подкручивает исходный размер массива для Эратосфена относительно n
N = 1
print(f'{"_" * 30} {N=} {"_" * 30}')
print(timeit('prime_num_brut(N)', number=100, globals=globals()))  # 0.00033660000000000287
print(timeit('eratosthenes(N, MAGIC_NUMBER)', number=100, globals=globals()))  # 0.0010409000000000009

MAGIC_NUMBER = 11  # подкручивает исходный размер массива для Эратосфена относительно n
N = 10
print(f'{"_" * 30} {N=} {"_" * 30}')
print(timeit('prime_num_brut(N)', number=100, globals=globals()))  # 0.0216991
print(timeit('eratosthenes(N, MAGIC_NUMBER)', number=100, globals=globals()))  # 0.013907799999999998

MAGIC_NUMBER = 11  # подкручивает исходный размер массива для Эратосфена относительно n
N = 100
print(f'{"_" * 30} {N=} {"_" * 30}')
print(timeit('prime_num_brut(N)', number=100, globals=globals()))  # 4.1459559
print(timeit('eratosthenes(N, MAGIC_NUMBER)', number=100, globals=globals()))  # 0.1587177000000004

MAGIC_NUMBER = 11  # подкручивает исходный размер массива для Эратосфена относительно n
N = 1000
print(f'{"_" * 30} {N=} {"_" * 30}')
print(timeit('prime_num_brut(N)', number=100, globals=globals()))  # 20.0159218
print(timeit('eratosthenes(N, MAGIC_NUMBER)', number=100, globals=globals()))  # 0.3240426999999997

MAGIC_NUMBER = 11  # подкручивает исходный размер массива для Эратосфена относительно n
N = 1000
print(f'{"_" * 30} {N=} {"_" * 30}')
run('prime_num_brut(N)')
run('eratosthenes(N, MAGIC_NUMBER)')

#       4 function calls in 0.202 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.202    0.202 <string>:1(<module>)
#      1    0.202    0.202    0.202    0.202 lesson_4_task_2.py:16(prime_num_brut)
#      1    0.000    0.000    0.202    0.202 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#       1341 function calls in 0.004 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#      1    0.003    0.003    0.003    0.003 lesson_4_task_2.py:31(eratosthenes)
#      1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:32(<listcomp>)
#      1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#   1335    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
