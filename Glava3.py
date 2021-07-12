# Глава 3

# y = 20
# if y == 20:
#     x = 0
# print(x)
# -------------------------------------------------
# sales = 10000
# if sales >= 10000:
#     comissonRate = 0.2
# print(comissonRate)
# -------------------------------------------------
#
# speed = int(input('Введите число: '))
# a = 0
# b = 200
#
# if speed < a or speed > b:
#     print('Число вне диапазона 0 - 200')
# else:
#     print('Число в диапозоне 0 - 200')
#
# if speed >= a and speed <= b:
#   print('Допустимое число')
# else:
#   print('Не допустимое')
# --------------------------------------------------
#
# x = int(input('Введите х = '))
#
# if x > 100:
#     y = 20
#     z = 40
#     print('true', y, z)
# else:
#     print('false')
#
# a = int(input('Введите a = '))
# -------------------------------------------
# if a < 10:
#     b = 0
#     c = 1
#     print('true', b, c)
# -------------------------------------------
# a = int(input('Введите a = '))
#
# if a < 10:
#     b = 0
#     print(b)
# else:
#     b = 99
#     print(b)
# ------------------------------------------------
# if score >= A_score:
#     print('Ваш уровень - А')
# else:
#     if score >= B_score:
#         print('Ваш уровень - В')
#     else:
#         if score >= C_score:
#             print('Ваш уровень - С')
#         else:
#             if score >= D_score:
#                 print('Ваш уровень - D')
#             else:
#                 print('Ваш уровень - F')
# ----------------------------------------------------

# amount1 = int(input('Введите am1: '))
# amount2 = int(input('Введите am2: '))
#
# if amount1 > 10 and amount2 < 100:
#     if amount1 > amount2:
#         print(amount1)
#     else:
#         print(amount2)
# -------------------------------------------------------
#
# speed = int(input('speed = '))
#
# if speed >= 24 and speed <= 56:                  # if 24 <= speed <= 56: - так лучше
#     print('Speed is normal')
# else:
#     print('Speed is dangerous')
# --------------------------------------------------------
#
# points = int(input('point = '))
#
# if points < 9 or points > 51:
#     print('Недопустимые точки')
# else:
#     print("Допустимые точки")
# --------------------------------------------------------
#
# import turtle
# if turtle.heading() >= 0 and turtle.heading() <= 45:
#     turtle.penup()
#     print('penUP')
#     turtle.done()

# ------------------------------------

# if turtle.pencolor() == 'black':
#     turtle.pencolor('blue')
#     print('Set blue')


# import turtle
#
# if turtle.pencolor() == 'black':
#      turtle.pencolor('blue')
#
# if turtle.pencolor() == 'blue' or turtle.pencolor() == 'red':
#     turtle.pensize(5)
#     print('done')
# else:
#     print('nope')
# -------------------------------------------------------------

# Блок с задачами.

# 1. День недели.
#
# PONED = 1
# VTOR = 2
# SREDA = 3
# CHETVG = 4
# PYATNICA = 5
# SUBB = 6
# VOSKR = 7
#
# num = int(input('Выберите день недели от 1 до 7: '))
#
# if num >= PONED and num <= VOSKR:                   # PONED <= num <= VOSKR: - альтернатива упрощения
#     if num == PONED:
#         print('Понедельник')
#     elif num == VTOR:
#         print('Вторник')
#     elif num == SREDA:
#         print('Среда')
#     elif num == CHETVG:
#         print('Четверг')
#     elif num == PYATNICA:
#         print('Пятница')
#     elif num == SUBB:
#         print('Суббота')
#     elif num == VOSKR:
#         print('Воскресенье')
# else:
#     print('Введите число от 1 до 7')
#
# --------------------------------------------
#
# 2. Площадь прямоугольников.
# S = D * W
# p1d = int(input('Введите длину 1 прямоугольника: '))
# p1w = int(input('Введите ширину 1 прямоугольника: '))
# p2d = int(input('Введите длину 2 прямоугольника: '))
# p2w = int(input('Введите ширину 2 прямоугольника: '))
#
# S1 = p1d * p1w                 # Площадь первого
# S2 = p2d * p2w                 # Площадь второго
#
# if S1 > S2:
#     print('\n', 'Площадь первого больше площади второго:', 'Первый:', S1, 'Второй:', S2, sep=' ')
# elif S1 == S2:
#     print('\n', 'Площадь первого равна площади второго:', 'Первый:', S1, 'Второй:', S2, sep=' ')
# elif S2 > S1:
#     print('\n', 'Площадь второго больше площади первого:', 'Второй:', S2, 'Первый:', S1, sep=' ')
# elif S2 == S1:                                                                                         # не
#     print('\n', 'Площадь второго равна площади первого:', 'Второй:', S2, 'Первый:', S1, sep=' ')       # обязательно
# --------------------------------------------------------------------------------------------------------
#
# 3. Классификатор возраста.
#
# vozrast = int(input('Введите возвраст человека: '))
#
# if vozrast <= 1:
#     print('Это младенец')
# elif 1 < vozrast < 13:
#     print('Ребёнок')
# elif 13 < vozrast < 20:
#     print('Подросток')
# elif vozrast > 20:
#     print('Взрослый')
# -------------------------------------
#
# 4. Римские цифры
#
# I = 1
# II = 2
# III = 3
# IV = 4
# V = 5
# VI = 6
# VII = 7
# VIII = 8
# IX = 9
# X = 10
#
# chislo = int(input('Введите число от 1 до 10: '))
#
# if chislo == I:
#     print('Римская I')
# elif chislo == II:
#     print('Римская II')
# elif chislo == III:
#     print('Римская III')
# elif chislo == IV:
#     print('Римская IV')
# elif chislo == V:
#     print('Римская V')
# elif chislo == VI:
#     print('Римская VI')
# elif chislo == VII:
#     print('Римская VII')
# elif chislo == VIII:
#     print('Римская VIII')
# elif chislo == IX:
#     print('Римская IX')
# elif chislo == X:
#     print('Римская X')
# else:
#     print('Ошибка, введите число от 1 до 10')
# --------------------------------------------------------------------
#
# 5. Масса и вес
# вес = масса * 9.8
# mass = float(input('Введите массу тела: '))
#
# ves = mass * 9.8
#
# if ves > 500:
#     print('Вес слишком тяжелый -', format(ves, ',.2f'), 'Ньютонов')
# elif ves < 100:
#     print('Вес слишком легкий -', format(ves, ',.2f'), 'Ньютонов')
# else:
#     print('Вес средний -', format(ves, ',.2f'), 'Ньютонов')
# --------------------------------------------------------------------
#
# 6. Волшебные даты
#
# data = int(input('Введите дату: '))
# month = int(input('Введите месяц: '))
# year = int(input('Введите год: '))
#
# summ = data * month
#
# if summ == year:
#     print('Это волшебная дата')
# else:
#     print('Это не волшебная дата')
# --------------------------------------------------------------------
#
# 7. Цветовой микшер
# RED_BLUE = 'Фиолетовый'
# RED_YELLOW = 'Оранжевый'
# BLUE_YELLOW = 'Зелёный'
#
# color = input('Выберите 2 цвета из красного, синего и желтого: \n')
#
# fiolet = 'красный + синий'
# orange = 'красный + желтый'
# green = 'синий + желтый'
#
# if color == fiolet:
#     print(RED_BLUE)
# elif color == orange:
#     print(RED_YELLOW)
# elif color == green:
#     print(BLUE_YELLOW)
# else:
#     print('Таких цветов нет в базе!')
# ------------------------------------------------------------------------------------------
#
# 8. Калькулятор сосисок для пикника.
# МОИ ПОПЫТКИ, ПОЧТИ РЕШИЛ, НО ЗАШЕЛ В ТУПИК:

# friends = int(input('Сколько участников пикника? '))
# Porcia = int(input('Количество хот-догов, предложенное каждому участнику: '))
#
# PackSos = 10
# PackBul = 8
#
# AllPool = Porcia * friends
#
# if AllPool >= PackBul:
#     minBul = AllPool // PackBul + 1
#     ostBul = minBul * PackBul - AllPool
#     print('Минимальное количество упаковок булочек - ', minBul)
#     print('Остаток булочек составит - ', ostBul)
# else:
#     minBul = AllPool // 8
#
# if AllPool >= PackSos:
#     minSos = AllPool // PackSos + 1
#     ostSos = minSos * PackSos - AllPool
#     print('Минимальное количество упаковок сосисок - ', minSos)
#     print('Остаток сосисок составит - ', ostSos)

# ПРАВИЛЬНОЕ РЕШЕНИЕ:
# hotdogs = int(input("How many? "))
#
# dog_u = hotdogs // 10 if hotdogs % 10 == 0 else hotdogs // 10 + 1
# bul_u = hotdogs // 8 if hotdogs % 8 == 0 else hotdogs // 8 + 1
#
# print('Упаковок сосисок: ', dog_u)
# print('Осталось сосисок: ', dog_u * 10 - hotdogs)
# print('Упаковок булок: ', bul_u)
# print('Осталось булок: ', bul_u * 8 - hotdogs)
#
# ----------------------------------------------------------------------
#
# 9. Цвета колеса рулетки.
#
# Enter = int(input('Введите число от 0 до 36: '))
#
# if Enter > 36 or Enter < 0:
#     print('Ошибка ввода')
# if Enter == 0:
#     print('Зелёный')
# if 1 <= Enter <= 10:
#     if Enter % 2 == 0:
#         print('Черный')
#     else:
#         print('Красный')
# if 11 <= Enter <= 18:
#     if Enter % 2 == 0:
#         print('Красный')
#     else:
#         print('Черный')
# if 19 <= Enter <= 28:
#     if Enter % 2 == 0:
#         print('Черный')
#     else:
#         print('Красный')
# if 29 <= Enter <= 36:
#     if Enter % 2 == 0:
#         print('Красный')
#     else:
#         print('Черный')
#
# --------------------------------------------------------------------
#
# 10. Игра в подсчитывание монет.
#
# m5 = int(input('Введите количество монет номиналом 5: '))
# m10 = int(input('Введите количество монет номиналом 10: '))
# m50 = int(input('Введите количество монет номиналом 50: '))
#
# x5 = m5 * 5
# x10 = m10 * 10
# x50 = m50 * 50
#
# summ = x5 + x10 + x50
#
# if summ == 100:
#     print(summ, '- Вы победили, это рубль!')
# if summ > 100:
#     print(summ, '- больше рубля')
# if summ < 100:
#     print(summ, '- меньше рубля')
# -------------------------------------------------------------------------
#
# 11. Очки книжного клуба
#
#
# n = int(input('Сколько книг вы купили за этот месяц? '))
#
# if n == 0:
#     print('Вы заработали 0 очков')
# elif n == 2:
#     print('Вы заработали 5 очков!')
# elif n == 4:
#     print('Вы заработали 15 очков!')
# elif n == 6:
#     print('Вы заработали 30 очков!')
# elif n >= 8:
#     print('Вы заработали 60 очков!')
# else:
#     print('Не хватает 1 книги для следующего уровня.')
#
# -----------------------------------------------------------------
#
# 12. Реализация ПО
#
# Buy = int(input('Сколько пакетов нашего ПО вы купили? '))
#
# price = Buy * 99
# print('Цена без скидки:', price)
#
# if 10 <= Buy <= 19:
#     sale10 = price * 0.1
#     lastPrice = price - sale10
#     print('Сумма скидки 10% = ', format(sale10, ',.2f'), '\n',
#           'Итоговая цена - ', format(lastPrice, ',.2f'), sep='')
# if 20 <= Buy <= 49:
#     sale20 = price * 0.2
#     lastPrice = price - sale20
#     print('Сумма скидки 20% = ', format(sale20, ',.2f'), '\n',
#           'Итоговая цена - ', format(lastPrice, ',.2f'), sep='')
# if 50 <= Buy <= 99:
#     sale30 = price * 0.3
#     lastPrice = price - sale30
#     print('Сумма скидки 30% = ', format(sale30, ',.2f'), '\n',
#           'Итоговая цена - ', format(lastPrice, ',.2f'), sep='')
# if Buy > 100:
#     sale40 = price * 0.4
#     lastPrice = price - sale40
#     print('Сумма скидки 40% = ', format(sale40, ',.2f'), '\n',
#           'Итоговая цена - ', format(lastPrice, ',.2f'), sep='')
# --------------------------------------------------------------------------
#
# 13. Стоимость доставки
#
# mass = int(input('Введите массу пакета(г): '))
#
# if mass <= 200:
#     price = mass / 100 * 150
#     print('Цена доставки составит -', format(price, '.0f'))
# if 200 < mass < 600:
#     price = mass / 100 * 300
#     print('Цена доставки составит -', format(price, '.0f'))
# if 600 < mass <= 1000:
#     price = mass / 100 * 400
#     print('Цена доставки составит -', format(price, '.0f'))
# if mass > 1000:
#     price = mass / 100 * 475
#     print('Цена доставки составит -', format(price, '.0f'))
# ---------------------------------------------------------------------------------
#
# 14. Индекс массы тела.
# ИМТ = масса / (рост * рост)           # в книге формула не до конца верная ( имт = масса / рост )
#
# mass = int(input('Введите массу тела(кг): '))
# rost = float(input('Введите рост(метры): '))
#
# index = mass / (rost * rost)
# print('ИМТ =', format(index, '.2f'))
#
# if index < 18.5:
#     print('Ваш вес ниже нормы!')
# elif 18.5 < index < 25:
#     print('Ваш вес в пределах нормы.')
# elif index > 25:
#     print('Ваш вес выше нормы!')
# --------------------------------------------------------------------------------
#
# 15. Калькулятор времени
# Я хз.
# total = int(input('Введите количество секунд: '))
#
# if total >= 60:
#     min = total // 60
#     sec = total % 60
#     print(min, 'мин.', sec, 'сек.')
# elif total >= 3600:
#     hours = total // 3600
#     min = total // 60
#     sec = total % 60
#     print(hours, 'ч.', min, 'мин.', sec, 'сек.')
# elif total >= 86400:
#     days = total // 86400
#     hours = total // 3600
#     min = total // 60
#     sec = total % 60
#     print(days, 'д.', hours, 'ч.', min, 'мин.', sec, 'сек.')
# else:
#     print('<1')
#
# if total >= 60:
#     min = total // 60
#     sec = total % 60
#     if total >= 3600:
#         hours = (total // 3600) % 60
#     if total >= 86400:
#         days = total // 86400
# print(min, 'мин.', sec, 'сек.')
#  print(hours, 'ч.', min, 'мин.', sec, 'сек.')
#      print(days, 'д.', hours, 'ч.', min, 'мин.', sec, 'сек.')
#
# days1 =  (total // 86400 % 3600 % 60) % 60
# print(days1)
# ------------------------------------------------------------------------------------
#
# 16. Дни в феврале
#
# n = int(input('Введите год - '))
#
# if n % 100 == 0:
#     if n % 400 == 0:
#         print('Visok god, 29 days')
#     else:
#         print('Dflt, 28 days.')
# if n % 100 != 0:
#     if n % 4 == 0:
#         print('Visok, 29 days')
#     else:
#         print('28 days, deflt')
#
# ------------------------------------------------------------------------------------------
#
# 17. Диагностическое дерево качества вай фай
#
# print('Перезагрузите ПК и попробуйте подключиться', '\n')
#
# fix = input('Вы исправили проблему? ')
#
# if fix == 'Нет' or fix == 'нет':
#     print('Перезагрузите маршрутизатор и попробуйте подключиться', '\n')
#     fix = input('Вы исправили проблему? ')
#     if fix == 'Нет' or fix == 'нет':
#         print('Убедитесь, что кабели между маршрутизатором и модемом прочно подсоединены', '\n')
#         fix = input('Вы исправили проблему? ')
#     if fix == 'Нет' or fix == 'нет':
#         print('Переместите маршрутизатор на новое место', '\n')
#         fix = input('Вы исправили проблему? ')
#     if fix == 'Нет' or fix == 'нет':
#         print('Возьмите новый маршрутизатор')
# else:
#     print('Вы молодец!')
# ----
# n = int(input())
#
# print('The next number for the number ', n, ' is ', n + 1, '.', '\n',
#       'The previous number for the number ', n, ' is ', n - 1, '.', sep='')
# ---------------------------------------------------------------------------
# count = 10
# while count < 100:
#       print('hi world')
#       exit()
# ---------------------------------------------------------------------------
# for x in range(2,6):
#     print(x)

# --hren' ne iz knigi
# if True > False != True:
#     print(True)
# else:
#     print(False)
#
# n = 'bar'
# m = 'foo'
#
# print('barf' in 2 * (m+n))
# ----------------------------------------
#
