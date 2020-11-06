# https://drive.google.com/file/d/1S66W7HhFSdi1-C_RDhv0ZOrRDSHmF52y/view?usp=sharing

# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.


def my_f(num):
    """Возращает число с обратным расположением цифр относительно числа num"""
    if num // 10 == 0:
        return str(num)
    n = num % 10
    return str(n) + my_f(num // 10)


if __name__ == '__main__':
    a = int(input('Ведите вещественное число: '))
    a_r = int(my_f(a))
    print(a_r)
