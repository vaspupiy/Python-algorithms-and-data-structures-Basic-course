# https://drive.google.com/file/d/1udTCq6-gPpIhv477x7aTpk-aKRozgSj0/view?usp=sharing

# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

SHIFT = 96
print('Укажите номер буквы.')
num_l = int(input('Введите целое число от 1 до 26: '))
code_l = num_l + SHIFT
l = chr(code_l)
print(f'Это буква {l}.')
