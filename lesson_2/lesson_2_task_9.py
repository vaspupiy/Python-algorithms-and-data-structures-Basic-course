# https://drive.google.com/file/d/1S66W7HhFSdi1-C_RDhv0ZOrRDSHmF52y/view?usp=sharing

# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def my_f(a):
    """Возвращает сумму цифр натурального числа a"""
    assert len(str(a)) < 999, 'Слишком длинное число'  # добавлено с учетом знаний полученных на лекции
    if a // 10 == 0:
        return a
    return a % 10 + my_f(a // 10)


if __name__ == '__main__':
    n_max, s_max = 0, 0
    while True:
        num_a = int(input('Введите натуральное число, для завершения введите 0: '))
        if num_a == 0:
            break
        s_a = my_f(num_a)
        if s_a > s_max:
            n_max = num_a
            s_max = s_a
    print(f'Самое большое из введенных чисел по сумме цифр - число {n_max},сумма его цифр = {s_max} ')
