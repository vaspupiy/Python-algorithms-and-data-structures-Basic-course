# https://drive.google.com/file/d/1S66W7HhFSdi1-C_RDhv0ZOrRDSHmF52y/view?usp=sharing

# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

def my_f_1(num, count_num):
    """Возвращает ввиде строки пары код-символ таблицы ASCII в количестве count_num начиная с num (шаг 1)  """
    out_str = ''
    for i in range(count_num):
        out_str += f'{num}-"{chr(num)}" '
        num += 1
    return out_str.rstrip()


def my_f_2(num, count_num):
    """Выводит на экран в одну строку пары код-символ таблицы ASCII в количестве count_num начиная с num (шаг 1)  """
    for i in range(count_num - 1):
        print(f'{num}-"{chr(num)}"', end=' ')
        num += 1
    print(f'{num}-"{chr(num)}"')
    return


if __name__ == '__main__':
    start = 32
    finish = 127
    step = 10
    while start + step <= finish:
        print(my_f_1(start, step))
        start += step
    print(my_f_1(start, finish - start + 1))

    print('\nvar2\n')

    start = 32
    finish = 127
    step = 10
    while start + step <= finish:
        my_f_2(start, step)
        start += step
    my_f_2(start, finish - start + 1)
