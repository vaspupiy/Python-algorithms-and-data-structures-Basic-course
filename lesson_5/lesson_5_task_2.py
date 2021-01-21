# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque


def test_my_f():
    test_ = ['1A1', '2B3', '193A', 'FC203', 'A19C', '2F3', '8DA34', '56EB']
    print('\nСложение:\n')
    for i in test_:
        for j in test_:
            print(hex(int(i, 16) + int(j, 16)), end=": ")
            print(''.join(sum_16(i, j, ENCRYPTION, DECRYPTION)), end=" - ")
            print('Ok' if (int(i, 16) + int(j, 16)) == int(''.join(sum_16(i, j, ENCRYPTION, DECRYPTION)),
                                                           16) else 'fault')
    print('\nУмножение:\n')
    for i in test_:
        for j in test_:
            print(hex(int(i, 16) * int(j, 16)), end=": ")
            print(''.join(multiply_16(i, j, ENCRYPTION, DECRYPTION)), end=" - ")
            print('Ok' if (int(i, 16) * int(j, 16)) == int(''.join(multiply_16(i, j, ENCRYPTION, DECRYPTION)),
                                                           16) else 'fault')


def sum_16(num_1, num_2, enc, dec, n_system=16):
    sum_ = deque()
    num_1 = deque(num_1)  # буду выравнивать длину списков добавляя 0-и в начало списка... по этому deque()
    num_2 = deque(num_2)  # ... и вообще буду делать всякое такое, что изменило бы подаваемый на вход список
    if len(num_1) != len(num_2):
        delta = len(num_1) - len(num_2)
        if delta > 0:
            num_2.extendleft('0' * delta)
        else:
            num_1.extendleft('0' * abs(delta))
    t = 0  # то, что "запоминаем в уме" при сложении
    for _ in range(len(num_1)):
        s = enc[num_1.pop()] + enc[num_2.pop()] + t
        t = s // n_system
        sum_.appendleft(dec[s % n_system])
    if t:
        sum_.appendleft(dec[t])
    # return ''.join(sum_)  # Увидел, что выводить нужно список :(
    return list(sum_)  # По заданию вывод ввиде списка пример: [‘C’, ‘F’, ‘1’]


def multiply_16(num_1, num_2, enc, dec, n_system=16):
    # num_1 = tuple(num_1)  # Обращаюсь по индексу, и не меняю... и по этому решил, что даже не list()
    # num_2 = tuple(num_2)  # :(  Увидел, что изначально нужно сохранять, и сохранять в ввиде списка...
    multiply = deque()
    for i in range(len(num_1) - 1, -1, -1):
        temp = deque()  # хранит временную стоку - результат перемножения каждой цифры разряда на число
        temp.extend([0] * (len(num_1) - 1 - i))  # добавляю количесво 0 в зависимости от позиции i (сдвиг разряда)
        tm = 0  # то, что "запоминаем в уме" при умножении
        for j in range(len(num_2) - 1, -1, -1):
            m = enc[num_1[i]] * enc[num_2[j]] + tm
            tm = m // n_system
            temp.appendleft(m % n_system)
        if tm:
            temp.appendleft(tm)
        multiply.extendleft([0] * (len(temp) - len(multiply)))
        s_temp = deque()
        ts = 0  # то, что "запоминаем в уме" при сложении
        for _ in range(len(temp)):
            s = multiply.pop() + temp.pop() + ts
            ts = s // n_system
            s_temp.appendleft(s % n_system)
        if ts:
            s_temp.appendleft(ts)
        multiply = s_temp
    # return ''.join(dec[i] for i in multiply) # Увидел, что выводить нужно список :(
    return [dec[i] for i in multiply]


if __name__ == '__main__':
    ENCRYPTION = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                  '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    # DECRYPTION = {i: k for k, i in ENCRYPTION.items()}
    DECRYPTION = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
                  9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    NUM_SYSTEM = 16
    # test_my_f()
    a = list(input('Введите первое число: ').strip().upper())
    b = list(input('Введите второе числое: ').strip().upper())
    print(f'{a} + {b} = {(sum_16(a, b, ENCRYPTION, DECRYPTION))}')
    print(f'{a} * {b} = {(multiply_16(a, b, ENCRYPTION, DECRYPTION))}')
    print(f'\nпроверка на сохранность введенных чисел после вычислений:\nпервое число :{a},\nвторое число :{b}')
