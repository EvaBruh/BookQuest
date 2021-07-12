# Глава 4

# Алгоритмический тренажёр
#
# product = 0
#
# while product < 100:
#     count = int(input('Введите число: '))
#     product = count * 10
#     print('Итого:', product)
#
# -------
#
# more = 'д'
#
# while more == 'д':
#     x = int(input('Введите первое число: '))
#     c = int(input('Введите второе число: '))
#     summ = x+c
#     print('Сумма: ', summ)
#     more = input('Ещё разок? Введите ''д'', если Да: ')
# -------
#
# for x in range(0, 1010, 10):
#   print(x)
# -------
#
# total = 0.0
# for x in range(10):
#     z = int(input('Введите число: '))
#     total += z
#     print(total)
# --------------
# pipec tupil tut dolgo
# total = 0.0
# for x in range(1, 31):
#     total += x / (31 - x)
#     print(total)
# --------------
#
# x += 1
# x *= 2
# x /= 10
# x -= 100
# --------------
#
# for rows in range(10):
#     for col in range(15):
#             print('#', end='')
#     print()
# --------------
#
#
# x = int(input('Enter number: '))
#
# while x < 0:
#     print('Error!')
#     x = int(input('Enter correct number, please: '))
#
# ---------
#
# x = int(input('Enter number 1 - 100: '))
#
# while x < 1 or x > 100:
#     print('Error, enter correct number, please!')
#     x = int(input('Enter: '))
# --------------
# Задачки

# 1. Сборщик ошибок
#
# total = 0
#
# for days in range(5):
#     error = int(input('Сколько ошибок сегодня собрал? '))
#     total += error
#     print('Текущее количество ошибок:', total)
# print('\nОшибок за 5 дней собрано:', total)
#
# -----------------------------------
#
# 2.  Сожженные калории.
#     4.2 калории в минуту
#
# print('Сколько Ккал сгорит за 10, 15, 20, 25, 30 минут бега', '\n')
# for min in range(10, 31, 5):
#     time = min * 4.2
#     print('Сожжено Ккал:', time)
#
# -----------------------------------
#
# 3. Анализ бюджета.
#
# cash = float(input('Сумма на месяц: '))
# total = 0.0
#
# rashod = float(input('Введите сумму расхода на категорию (п. Здоровье/Еда/Спорт): '))
# total += rashod
#
# eco = cash - total
# pererashod = total - cash
# print('Общий расход: ', total)
#
# if total < cash:
#     print('Экономия: ', eco)
# else:
#     print('Перерасход: ', pererashod)
# --------------------------------------------------------
#
# 4. Пройденное расстояние
# Расстояние = скорость * время
#
# speed = float(input('Скорость (км): '))
# hours = int(input('Время (часы): '))
#
# print('Час', 'Пройденное расстояние', sep='\t')
# print('-------------------------')
#
# for s in range(hours):
#     km = speed * (s+1)
#     print(s+1, km, sep='\t')
#
# --------------------------------------------------
#
# 5. Средняя толщина дождевых осадков
#
# skok_let = int(input('За сколько лет? '))
# all_mm = 0.0
#
# for year in range(skok_let):
#     for month in range(1, 13):
#         mm = int(input('Сколько мм? '))
#         all_mm += mm
#         all_month = skok_let * month
#         average = all_mm / all_month
#
# print('Количество месяцев:', all_month, '\n',
#       'Общее количество дождевых осадков за всё время:', all_mm, '\n'
#       'Средняя толщина осадков за всё время:', format(average, '.2f'))
# ----------------------------------------------------------------------
#
# 6. Таблица соответствия между градусами Цельсия и Фаренгейта.
#
# print('Таблица температуры соответствия Цельсия и Фаренгейта')
# print('C\tF')
#
# for temperature in range(0, 21):
#     tempF = 9 / 5 * temperature + 32
#     print(temperature, '\t', format(tempF, ',.1f'), sep='')
#
# ---------------------------------------
#
# 7. Мелкая монета для зарплаты
#
# days = int(input('Введите количество дней:'))
#
# day = 0.01
# zp_itog = 0.01
# multiply = 2
#
# print('Дни\t Зарплата')
# for one_day in range(1, days):
#     day *= multiply
#     zp_itog += day
#     print(one_day+1, '\t', format(day, ',.2f'))
#     all_days = one_day
#
# nal = zp_itog * 0.13                             # 13% - ставка налога
# zp = zp_itog - nal
# print('Итоговая сумма налога в 13%:', format(nal, ',.2f') +
#       '\nВаша зарплата в рублях за', days+1, 'дней:'
#       '\nДо вычета налогов:', format(zp_itog, ',.0f'),
#       '\nПосле вычета налогов:', format(zp, ',.0f'))

# ---------------------------------------------
#
# 8. Сумма чисел
# count = 1
# summ = 0
# while count > 0:
#     count = int(input('Введите положительное число: '))
#     summ += count
# print('Сумма введенных чисел равна: ', summ)
#
# --------------------------------------------------
# 9. Уровень океана
#
# mm = 0.0
# print('Год\t', 'Количество мм.')
# for years in range(1, 26):
#     mm += 1.6
#     print(years, '\t', format(mm, '.1f'))
# ---------------------------------------------
# 10. Рост платы за обучение
#
# price = 45000
# stavka = 0.03
# for year in range(2, 6):
#     price_stavki = price * stavka               # сумма самой ставки
#     price += price_stavki
#     print(format(year, '.0f'), format(price, ',.0f'))
# -------------------------------------------
#
# 11. Потеря массы
#
# one_month = 1.5         # 1.5 КГ (500калорий-диета)
# ves = float(input('Введите свой вес: '))
#
# print('Месяц', '\t', 'Ожидаемый вес')
# for month in range(1, 7):
#     ves -= one_month
#     print(month, '\t\t', ves)
#
# --------------------------------------------
# 12. Вычисление факториала числа
#
# t = 1
# n = int(input('Введите целое неотрицательное число: '))
# while n <= 0:
#     n = int(input('Неверное значение, введите целое неотрицательное число: '))
# for factorial in range(1, n+1):
#     t *= factorial
# z = t
# print(z)
#
# -----------------------------------------------
#
# 13. Популяция
#
# start_value = int(input('Стартовое количество организмов:'))
# percent = int(input('Среднесуточное увеличение в %: '))
# days = int(input('Количество дней для размножения: '))
#
# reform = (100 + percent) / 100
#
# print('День\t Популяция')
# for pop in range(1, days):
#     start_value *= reform
#     print(pop+1, '\t\t', format(start_value, '.2f'))
#
# ----------------------------------------------------------
# 14. Рисование символов вложенные циклы.
# for row in range(8):
#     for col in range(row):
#         print('*', end='')
#     print('*')
# ------------------------------
# for row in range(8, 1, -1):
#     for col in range(row-2):
#         print('*', end='')
#     print('*')
# ------------------------------    ЭТОТ ХЗ КАК (стр 246 pdf)
# for row in range(8):
#     for col in range(row):
#         print(' ', end='')
#     print('*')
# # ------------------------------  ПРИМЕР ОТ ЧЕЛА ИЗ ВК
# for i in range(6):
#     print('#'+i*' '+'#')
# ------------------------------
#











