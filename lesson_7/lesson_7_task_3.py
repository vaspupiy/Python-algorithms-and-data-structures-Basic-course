# 3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
#     Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива.

from random import randint


def partition(ar, st, f):
    """Сортиррует массив на элементы: <,> или = барьерному элементу. Возвращает индексы элементов = барьерному"""
    sap_el = ar[st]
    pointer_max = st
    for i in range(st + 1, f):
        if ar[i] <= sap_el:
            pointer_max += 1
            ar[pointer_max], ar[i] = ar[i], ar[pointer_max]
    pointer_min = st
    for i in range(st + 1, pointer_max + 1):
        if ar[i] < sap_el:
            pointer_min += 1
            ar[pointer_min], ar[i] = ar[i], ar[pointer_min]
    ar[st], ar[pointer_min] = ar[pointer_min], ar[st]
    return [pointer_min, pointer_max]


def m_index_array(arr, start, fin, med):
    """Находит в массиве медиану, да вообще любой элемент"""
    if start >= fin:
        return array[start]
    pointer = partition(arr, start, fin)
    if pointer[0] <= med <= pointer[1]:
        return arr[pointer[0]]
    elif start <= med < pointer[0]:
        return m_index_array(arr, start, pointer[0], med)
    else:
        return m_index_array(arr, pointer[1] + 1, fin, med)


if __name__ == '__main__':
    SIZE = 23
    N_MIN = -6
    N_MAX = 7
    NUM_ELEM = SIZE // 2 + 1   # номер элемента, хотя индексация с 0(можно было 1 не добавлять)
    array = [randint(N_MIN, N_MAX) for _ in range(SIZE)]
    print(f'медианой массива :\n{array} \n является число :{m_index_array(array, 0, len(array), NUM_ELEM - 1)}')
    print(sorted(array)[len(array) // 2])
    print(sorted(array))
