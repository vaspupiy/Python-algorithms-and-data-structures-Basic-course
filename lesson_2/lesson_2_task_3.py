# https://drive.google.com/file/d/1S66W7HhFSdi1-C_RDhv0ZOrRDSHmF52y/view?usp=sharing

# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.


def my_f(num):
    """Возращает число с обратным расположением цифр относительно числа num"""
    assert len(str(num)) < 999, 'Слишком длинное число'  # добавлено с учетом знаний полученных на лекции
    if num // 10 == 0:
        return str(num)
    n = num % 10
    return str(n) + my_f(num // 10)


def dean_alg_my_rf(num, res=0):
    """Без использования строк(добавлено после просмотра лекции)"""
    assert len(str(num)) < 999, 'Слишком длинное число'  # добавлено с учетом знаний полученных на лекции
    if num == 0:
        return res
    return dean_alg_my_rf(num // 10, res * 10 + num % 10)


if __name__ == '__main__':
    a = int(input('Ведите вещественное число: '))
    a_r = int(my_f(a))
    print(a_r)
    print('\nNew_vr:')
    print(dean_alg_my_rf(a))


# Самый быстрый способ разворота строки
# num = input('Ввод строки: ')
# res = num[::-1]  # num[start=0:stop=len(num):step=-1]
# print(res)
