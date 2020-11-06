# https://drive.google.com/file/d/1S66W7HhFSdi1-C_RDhv0ZOrRDSHmF52y/view?usp=sharing

# 7. Напишите программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
# где n — любое натуральное число.

def my_f(n, s=0, a=0):
    """Возвращает сумму последовательности 1+2+...+n """
    for i in range(n):
        a += 1
        s += a
    return s


if __name__ == '__main__':
    num = int(input('Введите натуральное число: '))
    s1 = my_f(num)
    s2 = num * (num + 1) / 2
    if s1 == s2:
        print(f'1+2+...+n = n(n+1)/2 при n = {num} - выполняется')
    else:
        print(f'1+2+...+n = n(n+1)/2 при n = {num} - не выполняется')
