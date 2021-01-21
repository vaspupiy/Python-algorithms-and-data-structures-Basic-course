# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

from random import randint

SIZE = 10
MIN_ITEM = -15
MAX_ITEM = 10

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

search_elem = None
pose = None

for i, item in enumerate(array):
    if item < 0:
        if not search_elem or (item > search_elem):
            search_elem = item
            pose = i

print(f'Максимальным отрицательным элементом в массиве: \n{array}\nявляется число:\n{search_elem}'
      f'\nПозиция в массиве:\n{pose}' if search_elem else f'Отрицательные элементы в отсутствуют массиве: \n{array}')
