# Глава 5

# Алгоритмический тренажёр
#
# x = int(input('Введите число - '))
#
#
# def times_ten(z):
#     result = z * 2
#     print(result)
#
#
# times_ten(x)
# --------------------------------
# def show_value(quantity):
#     print(quantity)
#
# show_value(12)
# --------------------------------
# def my_function(a, b, c):
#     d = (a+c) / b
#     print(d)
#
# my_function(a=2, b=4, c=6)
# --------------------------------
# import random
#
# rand = random.randint(1, 100)
# print(rand)
# --------------------------------
# number = float(input('Число: '))
#
# def half(arg):
#     res = arg / 2
#     return res
# result = half(number)
#
# print(result)
# --------------------------------
# def cube(num):
#     return num * num * num
#
# result = cube(4)
# print(result)
# --------------------------------
# number = int(input('Число - '))
#
#
# def times_ten(arg):
#     result = arg * 10
#     return result
#
#
# print(times_ten(number))
# --------------------------------
# def get_first_name():
#     first_name = (input('Имя -'))
#     return first_name
# print(get_first_name())
# ----------------------------------------- ДАЛЕЕ ЗАДАЧИ(ого)
# 1. Конвертер километров
# km = int(input('Введите км: '))
#
#
# def km_in_mile(km):
#     result = km * 0.6214
#     return
#
# print(km_in_mile(km))
# ----------------------------------------------
# 2. Модернизация программы расчёта налога с продаж.
#
# REG_NAL = 0.025                                 # региональный налог // именованная(е) константа(ы)
# FED_NAL = 0.05                                  # федеральный налог //
#
#
# def main():
#     value = int(input('Введите величину покупки: '))
#
#     all_nalog = all_nal(reg_nal(value), fed_nal(value))
#
#     print('Рег. налог:', reg_nal(value))
#     print('Фед. налог:', fed_nal(value))
#     print('Общий налог:', all_nalog)
#     print('Сумма к оплате:', payment(value, all_nalog))
#
#
# def reg_nal(value):
#     return value * REG_NAL
#
#
# def fed_nal(value):
#     return value * FED_NAL
#
#
# def all_nal(reg, fed):
#     return reg + fed
#
#
# def payment(value, nalog):
#     return value + nalog
#
#
# main()
# -----------------------------------------------------------
# 3. Какова стоимость страховки
#
# KOEFFICENT = 0.8
#
# price_house = int(input('Введите стоимость вашего дома: '))
#
#
# def raschet_strahovki(price):
#     return price * KOEFFICENT
#
#
# print(raschet_strahovki(price_house))
# -----------------------------------------------------------
# 4. Расходы на автомобиль
#
# credit = int(input('Кредит: '))
# strahovka = int(input('Страховка: '))
# benzin = int(input('Бензин: '))
# maslo = int(input('Масло: '))
# shina = int(input('Шины: '))
# tehObs = int(input('Тех. обслуживание: '))
#
#
# def rashod_mes(credit, strahovka, benzin, maslo, shina, tehObs):
#     return credit + strahovka + benzin + maslo +shina + tehObs
#
#
# mes = rashod_mes(credit, strahovka, benzin, maslo, shina, tehObs)
# print('Общие затраты на машину в месяц составили:', mes)
# god = mes * 12                                                      # 12 месяцев
# print('Общие затраты на машину в год составили:', god)
# -----------------------------------------------------------
# 5. Налог на недвигу
#
# OCEN_KOEF = 0.6  # 60% от фактической стоимости
# NALOG = 0.72  # 72 цента за каждые 100 долларов оценочной стоимости
#
#
# def raschet():
#     fact_price = int(input('Введите фактическую стоимость дома: '))
#
#     ocen_price = fact_price * OCEN_KOEF  # Получаем оценочную стоимость недвиги
#     nalog = ocen_price * NALOG / 100  # Получаем размер налога с оцен. стоимости
#     return print('Оценочная стоимость:', ocen_price, '\n'
#                  'Налог на оцен. стоимость:', nalog)
#
#
# raschet()
# -----------------------------------------------------------
# 6. Калории за счёт жиров и углеводов
#
# jir = float(input('Сколько жиров съели? '))
# yglevod = float(input('Сколько углеводов съели? '))
#
#
# def raschet_kkal(jir, yglevod):
#     kkal_jir = jir * 9
#     kkal_yglevod = yglevod * 4
#     all_kkal = kkal_jir + kkal_yglevod
#     return print('Kkal от жиров:', kkal_jir, '\n'
#                  'Kkal от углеводов:', kkal_yglevod, '\n'
#                  'Общее количество Kkal:', all_kkal)
#
#
# raschet_kkal(jir, yglevod)
# -----------------------------------------------------------
# 7. Сидячие места на стадионе
#
# PRICE_A = 20    # Цена за место класса А
# PRICE_B = 15    # Цена за место класса B
# PRICE_C = 10    # Цена за место класса C
#
#
# def profit():
#     class_a = int(input('Сколько билетов класса А было продано? '))
#     class_b = int(input('Сколько билетов класса B было продано? '))
#     class_c = int(input('Сколько билетов класса C было продано? '))
#
#     profit_A = class_a * PRICE_A
#     profit_B = class_b * PRICE_B
#     profit_C = class_c * PRICE_C
#     all_profit = profit_A + profit_B + profit_C
#     return print('Выручка с билетов класса А:', profit_A, '\n'
#                  'Выручка с билетов класса B:', profit_B, '\n'
#                  'Выручка с билетов класса C:', profit_C, '\n'
#                  'Общая выручка с продажи билетов:', all_profit)
#
#
# profit()
# -----------------------------------------------------------
# 8. Оценщик малярных работ
#                                       # 5 литров краски = одна банка
# ONE_HOUR = 2000                         # Плата за час работы 2000
# TEN_S = ONE_HOUR * 8                    # 10 кв.м. = 8ч работы и 5 литров краски
#
#
# def ocenka_rabot():
#     S_stena = int(input('Введите площадь поверхности окрашиваемой стены: '))
#     price_banki = int(input('Введите цену 5-литровой банки краски: '))
#
#     WorkPrice = S_stena / 10 * TEN_S
#     HoursNeed = WorkPrice // ONE_HOUR
#     BanokNeed = HoursNeed // 8
#     PriceKraski = price_banki * BanokNeed
#     allPrice = PriceKraski + WorkPrice
#     print('Банок краски нужно:', BanokNeed)
#     print('Часов на работу уйдёт:', HoursNeed)
#     print('Стоимость работы:', WorkPrice)
#     print('Стоимость краски:', PriceKraski)
#     print('Общая стоимость работ:', allPrice)
#
#
# ocenka_rabot()
# -----------------------------------------------------------
# 9. Месячный налог с продаж
#
# MUN_NAL = 0.025                 # Муниципальный налог 2.5%
# FED_NAL = 0.05                  # Федеральный налог 5%
#
# value = int(input('Объем с продаж за месяц составил: '))
#
#
# def nalogi(value):
#     mun_nal = value * MUN_NAL
#     fed_nal = value * FED_NAL
#     all_nal = mun_nal + fed_nal
#     return print('Сумма муниципального налога:', mun_nal, '\n'
#                  'Сумма федерального налога:', fed_nal, '\n'
#                  'Общий налог с продаж:', all_nal)
#
#
# nalogi(value)
# -----------------------------------------------------------
# 10. Футы в дюймы
#
# ONE_FOOT = 12                   # Один фут = 12 дюймов
#
# value = int(input('Введите количество футов: '))
#
#
# def feet_to_inches(foot):
#     d = foot / ONE_FOOT
#     print('Количество дюймов:', d)
#
#
# feet_to_inches(value)
# -----------------------------------------------------------
# 11-12. Математический тест
#
# import random
#
# num1 = random.randint(1, 5000)
# num2 = random.randint(1, 5000)
# result = num1 + num2
#
# print(' ', num1, '\n'
#       '+', num2)
#
# check = int(input('Введите ответ: '))
#
# while check != result:
#     print('Неверно!')                       # print('Неверно, ответ:', result) <-- по условию задачи.
#     check = int(input('Введите снова: '))
# else:
#     print('Верно! Вы молодец')
# -----------------------------------------------------------
# 13. Максимальное из двух значений
#
# num1 = int(input('Число 1: '))
# num2 = int(input('Число 2: '))
#
#
# def max(num1, num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2
#
#
# print(max(num1, num2))
# -----------------------------------------------------------
# 14. Высота падения
# d = 1/2gt^2
# g = 9.8
#
#
# def main():
#     for i in range(1, 11):
#         print(falling_distance(i))
#
#
# def falling_distance(t):
#     d = 1 / 2 * g * t ** 2
#     return d
#
#
# main()
# -----------------------------------------------------------
# 15. Кинетическая энергия
# Ke = 1/2mv^2 m - massa / v - speed
#
# m = int(input('Введите массу: '))
# v = int(input('Введите скорость: '))
#
#
# def kinetic_energy(m, v):
#     k = 1 / 2 * m * v ** 2
#     return k
#
#
# print(kinetic_energy(m, v))
# -----------------------------------------------------------
# 16. Средний балл и его уровень
#
# def main():
#     avg = 0
#     print('Введите 5 оценок.')
#
#     for i in range(5):
#         num = int(input('Оценка: '))
#         avg += num
#         determine_grade(num)
#     calc_average(avg)
#
#
# def calc_average(avg1):
#      return print('Среднее значение оценок:', avg1 / 5)
#
#
# def determine_grade(num):
#     if num >= 90:
#         print('A')
#     elif 80 <= num <= 89:
#         print('B')
#     elif 70 <= num <= 79:
#         print('C')
#     elif 60 <= num <= 69:
#         print('D')
#     else:
#         print('F')
#
#
# main()
# ---------------------------------------------------------------
# 17. Счётчик чётных и нечётных чисел
#
# import random
# even = 0
# odd = 0
#
# for i in range(100):
#     value = random.randint(1, 100)
#     print(value)
#
#     if value % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#
# print('Чётных:', even,'\nНечётных:', odd)
# ---------------------------------------------------------------
# 18-19. Простые числа
#
# for n in range(2, 10):
#     is_prime = True
#
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals to', x, '*', n // x)
#             is_prime = False
#             break
#
#     if is_prime:
#         print(n, 'is a prime number')
#
# ---------------------------------------------------------------
# 20. Будущая стоимость. Незнаю, так или нет. -_-

# F = P * (1+i)^2
# p = int(input('Текущая сумма: '))
# i = int(input('Ставка: '))
# t = int(input('Количество месяцев: '))
#
#
# def dohod(p, i, t):
#     proc = i / 100
#     f = p * (1+proc)**2
#     print(f)
#     return f / t
#
#
# print(dohod(p, i, t))
# ---------------------------------------------------------------
# 21. Игра в угадывание случ. числа
#
# import random
#
#
# def main():
#
#     def prohod():
#         x = random.randint(1, 100)
#         # print(x)
#         loop = 1
#         n = int(input('Угадайте число: '))
#
#         while x > n or x < n:
#             if x < n:
#                 n = int(input('Слишком много, попробуйте ещё раз: '))
#                 loop += 1
#             else:
#                 n = int(input('Слишком мало, попробуйте ещё раз: '))
#                 loop += 1
#         else:
#             print('Win!')
#             print('Догадок:', loop)
#             next = input('Сыграем? (д/н): ')
#             while next == 'д':
#                 prohod()
#             else:
#                 print('До свидания!')
#     prohod()
#
#
# main()
# ---------------------------------------------------------------
# 22. Камень, ножницы, бумага
# import random
#
#
# def game():
#     user = input('Камень, Ножницы, Бумага? ')
#     x = random.randint(1, 3)
#     # print(x)
#     if user == 'Камень' and x == 2:
#         print('Выбор бота: Ножницы')
#         print('Камень бьёт Ножницы')
#     elif user == 'Ножницы' and x == 3:
#         print('Выбор бота: Бумага')
#         print('Ножницы бьют Бумагу')
#     elif user == 'Бумага' and x == 1:
#         print('Выбор бота: Камень')
#         print('Бумага бьет Камень')
#     elif user == 'Камень' and x == 1:
#         input('Ничья! Нажмите Enter, чтобы начать новый раунд.')
#         game()
#     elif user == 'Ножницы' and x == 2:
#         input('Ничья! Нажмите Enter, чтобы начать новый раунд.')
#         game()
#     elif user == 'Бумага' and x == 3:
#         input('Ничья! Нажмите Enter, чтобы начать новый раунд.')
#         game()
#     else:
#         print('Вы проиграли, бот выбрал', x, '\n'
#               '1 - Камень, 2 - Ножницы, 3 - Бумага')
# game()
