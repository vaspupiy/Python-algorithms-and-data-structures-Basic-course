# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

SIZE_ROW = 5
SIZE_COLUMN = 4

matrix = []

for _ in range(SIZE_ROW):
    a = []
    s = 0
    for _ in range(SIZE_COLUMN - 1):
        num = int(input('Введите целое число: '))
        s += num
        a.append(num)
    print('Ok')
    a.append(s)
    matrix.append(a)

# print(*matrix, sep='\n')

print('\nНевероятно красивый вывод матрицы: \n')
for row in matrix:
    for item in row:
        print(f'{item:>6}', end='')
    print()
