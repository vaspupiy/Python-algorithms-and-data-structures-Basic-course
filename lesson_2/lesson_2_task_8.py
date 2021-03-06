# https://drive.google.com/file/d/1S66W7HhFSdi1-C_RDhv0ZOrRDSHmF52y/view?usp=sharing

# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

def my_cf(num, d):
    """Возвращает количество цифр d в числе num."""
    c = 0
    while num != 0:
        if d == num % 10:
            c += 1
        num //= 10
    return c


def my_f(n, d):
    """Запрашивает числа n-раз и возвращает общее количество цифр d в веденных числах."""
    c = 0
    for i in range(n):
        num = int(input('Введите натуральное число: '))
        c += my_cf(num, d)
    return c


if __name__ == '__main__':
    n_seq = int(input('Ведите длину последовательности чисел: '))
    digit = int(input('Ведите цифру, которую необходимо посчитать: '))
    print(f'цифра {digit} в введенной последовательности чисел встречается {my_f(n_seq, digit)} раз')
