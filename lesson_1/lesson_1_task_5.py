# https://drive.google.com/file/d/1udTCq6-gPpIhv477x7aTpk-aKRozgSj0/view?usp=sharing

# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

SHIFT = 96
print('Введиде две буквы латинского алфавита')
letter1, letter2 = input('Введите две буквы от a до z через пробел: ').split()
if letter1 == letter2:
    c_letter1 = ord(letter1)
    n_letter1 = c_letter1 - SHIFT
    print(f'Вы ввели две одинаковые буквы({letter1}), с позицией в алфавите = {n_letter1}\n'
          f'(Между одинаковыми буквами - буквы отсутствуют)')
else:
    c_letter1, c_letter2 = ord(letter1), ord(letter2)
    n_letter1, n_letter2 = c_letter1 - SHIFT, c_letter2 - SHIFT
    d = abs(c_letter1 - c_letter2) - 1
    print(f'Позиция в алфавите для первой буквы({letter1}) = {n_letter1}\n'
          f'Позиция в алфавите для второй буквы({letter2}) = {n_letter2}\n'
          f'Количество букв в алфавите между первой и второй буквой = {d}')
