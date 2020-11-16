# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import defaultdict


def name_unique_input(i_, dict_):
    """Проверяет на уникальность название предприятия"""
    while True:
        name_company = input(f'Введите название предприятия №{i_}: ')
        if name_company not in dict_:
            return name_company
        print(f'Данные для предприятия {name_company} уже введены')


N_QUARTER = 4

num_company = int(input('Ведите данные о количестве предприятий: '))
average_annual_profits = defaultdict(float)
average_all_company_profits = 0

for i in range(1, num_company + 1):
    # company = input(f'Введите название предприятия №{i}: ')
    company = name_unique_input(i, average_annual_profits)
    for j in range(1, N_QUARTER + 1):
        quarter_profit = float(input(f'Введите прибыль предприятия {company} за {j}-й квартал: '))
        average_annual_profits[company] += quarter_profit / N_QUARTER
        average_all_company_profits += quarter_profit / N_QUARTER / num_company

print(f'\nСредняя прибыль (за год для всех предприятий): \n{average_all_company_profits}')


print(f'Перечень предприятий, чья прибыль выше среднего: ')
for item in average_annual_profits:
    if average_annual_profits[item] > average_all_company_profits:
        print(f'{item} - среднегодовая прибыль предприятия: {average_annual_profits[item]}')

# Выводить компании, чья прибыль = средней не просили... :)
# print(f'Перечень предприятий, чья прибыль равна средней: ')
# for item in average_annual_profits:
#     if average_annual_profits[item] == average_all_company_profits:
#         print(f'{item} - среднегодовая прибыль предприятия: {average_annual_profits[item]}')


print(f'Перечень предприятий, чья прибыль ниже среднего: ')
for item in average_annual_profits:
    if average_annual_profits[item] < average_all_company_profits:
        print(f'{item} - среднегодовая прибыль предприятия: {average_annual_profits[item]}')
