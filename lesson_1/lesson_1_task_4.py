# https://drive.google.com/file/d/1udTCq6-gPpIhv477x7aTpk-aKRozgSj0/view?usp=sharing

# Написать программу, которая генерирует в указанных пользователем границах:
# ● случайное целое число,
# ● случайное вещественное число,
# ● случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

from random import randint, uniform

print('Укажите границы случайного целого числа(включительно)')
a, b = map(int, input('введите два целых числа через пробел: ').split())
x = randint(a, b) if b > a else randint(b, a)
print(x)

print('Укажите границы случайного вещественного числа (включительно)')
a, b = map(float, input('введите два вещественных числа через пробел: ').split())
x = uniform(a, b) if b > a else randint(b, a)
print(x)

print('Укажите границы диапазона для  случайного символа')
symbol_1, symbol_2 = input('введите две строчные буквы латинского алфавита(от a до z) через пробел: ').split()
a, b = ord(symbol_1), ord(symbol_2)
x = randint(a, b) if b > a else randint(b, a)
y = chr(x)
print(y)  # print(chr(randint(ord(symbol_1), ord(symbol_2)) if b > a else randint(ord(symbol_2), ord(symbol_1))))
