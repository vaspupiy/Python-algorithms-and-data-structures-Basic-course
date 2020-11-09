# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

# NUM_MIN = 2
NUM_MAX = 99
DIGIT_MIN = 2
DIGIT_MAX = 9
count_item = 0

print(f'В диапазоне натуральных чисел от 2 до 99')
for i in range(DIGIT_MIN, DIGIT_MAX + 1):  # только при NUM_MIN = 2
    print(f'\tчислу {i} кратно {NUM_MAX // i:>3} чисел')

# # Алгоритм для проверки(наивный алгоритм) Работает при любом NUM_MIN (требует раскмонитить NUM_MIN = 2)
# count_item = 0
# dict_digit = {i: 0 for i in range(DIGIT_MIN, DIGIT_MAX + 1)}  # Наверное нужно как-то решить без словарей...
# for i in range(NUM_MIN, NUM_MAX + 1):
#     for j in dict_digit:
#         count_item += 1
#         if i % j == 0:
#             dict_digit[j] += 1
# print(dict_digit)
# print(count_item)
