# https://drive.google.com/file/d/1udTCq6-gPpIhv477x7aTpk-aKRozgSj0/view?usp=sharing

# Определить, является ли год, который ввел пользователь, високосным или не високосным.

print('Введите год, который хотите проверить на високосность.')
y = int(input('введите целое число: '))
if y % 4 != 0:
    print('Год не високосный.')
elif y % 100 != 0:
    print('Год високосный.')
elif y % 400 != 0:
    print('Год не високосный.')
else:
    print('Год високосный.')
