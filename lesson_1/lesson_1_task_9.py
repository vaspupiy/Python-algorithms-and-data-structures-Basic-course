# https://drive.google.com/file/d/1udTCq6-gPpIhv477x7aTpk-aKRozgSj0/view?usp=sharing

# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('Укажите 3-и различных числа:')
a, b, c = map(float, input('Введите три числа через пробел: ').split())
if a > b:
    if b > c:
        print(f'Среднее число {b}')
    elif a > c:
        print(f'Среднее число {c}')
    else:
        print(f'Среднее число {a}')
else:
    if c > b:
        print(f'Среднее число {b}')
    elif a > c:
        print(f'Среднее число {a}')
    else:
        print(f'Среднее число {c}')
