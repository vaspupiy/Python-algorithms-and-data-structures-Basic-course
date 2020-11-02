# https://drive.google.com/file/d/1udTCq6-gPpIhv477x7aTpk-aKRozgSj0/view?usp=sharing

# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.

print('Введите координаты первой точки')
x1, y1 = map(float, input('Введите через пробел значения х1 у1: ').split())
print('Введите координаты второй точки')
x2, y2 = map(float, input('Введите через пробел значения х2 у2: ').split())

if x2 - x1 == 0:
    if y2 - y1 == 0:
        print('Введены координаты точки')
    else:
        print(f'Прямая параллельна оси у, x = {x1}')
elif y2 - y1 == 0:
    print(f'Прямая параллельна оси x, y = {y1}')
else:
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    print(f'y = {k}x + {b}' if b != 0 else f'y = {k}x')
