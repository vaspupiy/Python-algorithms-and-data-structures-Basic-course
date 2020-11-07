# https://drive.google.com/file/d/1S66W7HhFSdi1-C_RDhv0ZOrRDSHmF52y/view?usp=sharing

# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def my_f(a, e=0, n=0):
    """Выводит на экран количиство четных - 'e' и не четных 'n' цифр в числе 'a'(a - натуральное число)."""
    a_ = a
    while a != 0:
        num = a % 10  # лишняя операция
        if num % 2 == 0:
            e += 1
        else:
            n += 1
    a //= 10  # Изменено после просмотра лекции (нарушение принципа DRY)
    print(f'В веденном числе "{a_}" количество четных цифр = {e}, количество не четных цифр = {n}')
    return


def dean_f(a, e=0, n=0):
    """Проведена работа над ошибками, в соотв. с замечанием преподавателя"""
    a_ = a
    while a != 0:
        if a % 2 == 0:
            e += 1
        else:
            n += 1
    a //= 10
    print(f'В веденном числе "{a_}" количество четных цифр = {e}, количество не четных цифр = {n}')
    return


if __name__ == '__main__':
    my_f(int(input('Введите натуральное число: ')))
    print('\nNex_def_vr:')
    dean_f(int(input('Введите натуральное число: ')))
