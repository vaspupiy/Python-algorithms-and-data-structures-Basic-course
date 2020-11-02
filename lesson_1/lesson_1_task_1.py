# https://drive.google.com/file/d/1udTCq6-gPpIhv477x7aTpk-aKRozgSj0/view?usp=sharing

# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

print("Введите 3-х значное число")
a = int(input('Введите число: '))

digit1 = a % 10
digit2 = a // 10 % 10
digit3 = a // 100
s = digit1 + digit2 + digit3
m = digit1 * digit2 * digit3
print(f"Сумма {s=}")
print(f"Произведение  {m=}")
