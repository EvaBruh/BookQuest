# Глава 2

# future_value = float(input('Введите желаемую сумму в будущем: '))
# rate = float(input('Введите годовой процент: '))
# years = int(input('Введите количество лет роста: '))
#
# PerRate = rate / 100
#
# present_value = future_value / (1.0 + PerRate) ** years
# print('Вам потребуется внести сумму: ', format(present_value, ',.2f'))

# ----------------------------------------------

# высчитывает экономию

# price = 200
#
# SALE = 0.5                                                  # именованная константа
# price_sale = price * SALE
# print('SALE:', (format(price_sale, '.0f')), end='%')
# ------------------------------------------------
# print('Задачки второй главы:\n')
#
# height = input('Ваш рост: ')
# print(height)
#
# color = input('Ваш любимый цвет: ')
# print(color)
# ----------------------------------------------------
# b = 2 + a
# a = b * 4
# b = a / 3.14
# a = b - 8

# total = 10 + 14
# down_payment = 5
# due = total - down_payment
# print(due)

# subtotal = 10
# total1 = subtotal * 0.15
# print(total1)
# ---------------------------------------------------------

# num = 99
# num = 5
# print(num)

# sales = 23.34532
# print(format(sales, '.2f'))
#
# number = 1234567.456
# print(format(number,',.1f'))
# -----------------------------------------------------------

# name = input('Name: ')
# adres = input('Adres: ')
# tel = input('Phone: ')
# speci = input('Speci: ')
#
# print('Your name -',name, '\nLive in -', adres, '\nPhone -', tel, '\nYour Speci. -', speci)
#-------------------------------------------------------------
# totalVal = input('Объем продаж по плану на год: ')
# ValTotal = int(totalVal)
# WIN_FL = 0.23
# profit = ValTotal * WIN_FL
# print(profit)
# ---------------------------------------------------------------
# QuadM = input('Введите размер участка в кв. метрах: ')
# IQuadM = int(QuadM)
# AKR_odin = 4047
# result = IQuadM / AKR_odin
# print(result)
# -----------------------------------------------------------------
#
#По сути это товарный чек
#
# apple = input('Цена яблока? ')
# appleInt = int(apple)
# banana = input('Цена банана? ')
# bananaInt = int(banana)
# milk = input('Цена молока? ')
# milkInt = int(milk)
# cocos = input('Цена кокоса? ')
# cocosInt = int(cocos)
# bread = input('Цена хлеба? ')
# breadInt = int(bread)
#
# SALE_NALOG = 0.07                                                # именованная константа налога с продажи в 7%
#
# summ = appleInt + bananaInt + milkInt + cocosInt + breadInt
# summNAL = summ * SALE_NALOG
# summALL = summNAL + summ
#
# print('Накопленная стоимость: ', format(summ, ',.2f'),'\n'
#       'Налоги: ', format(summNAL, ',.2f'), '\n'
#       'К оплате: ', format(summALL, ',.2f'))
#
#__________________________________________________________________________
#Path = 70 * 6
#print(Path)
# --------------------------------------------------------------------------
# value = input('Введите величину покупки: ')
# valueInt = int(value)
#
# FED_NAL = 0.05                                  # федеральный налог // именованная(е) константа(ы)
# REG_NAL = 0.025                                 # региональный налог //
#
# valFed = valueInt * FED_NAL
# valReg = valueInt * REG_NAL
# valNAL = valReg + valFed
#
# payment = valueInt + valNAL
#
# print('Покупка: ', format(valueInt, ',.2f'), '\n'
#       'Федеральный налог: ', format(valFed, ',.2f'), '\n'
#       'Региональный налог: ', format(valReg, ',.2f'), '\n'
#       'Общий налог: ', format(valNAL, ',.2f'), '\n'
#       'Сумма к оплате: ', format(payment, ',.2f'))
# ----------------------------------------------------------------------------
# расход = пройденные км / расход бензина в литрах
# km = input('Введите сколько пройдено км.: ')
# kmF = float(km)
# rashod = input('Введите расход в литрах: ')
# rashodF = float(rashod)
#
# result = kmF / rashodF
# print('Расход равен - ', format(result, ',.2f'))
# ---------------------------------------------------------------------------------

# eda = input('Введите стоимость еды: ')
# edaF = float(eda)
#
# CHAI = 0.18
# NAL = 0.07
#
# payCHAI = CHAI * edaF
# payNAL = NAL * edaF
#
# summ = payNAL + payCHAI + edaF
#
# print('Сумма к оплате: ', format(summ, ',.2f'), '\n'
#       'Чаевые: ', format(payCHAI, ',.2f'), '\n'
#       'Налоги: ', format(payNAL, ',.2f'))
# ------------------------------------------------------------------------------
#
# tempC = input('Введите температуру Цельсия: ')
# ftempC = float(tempC)
#
# tempF = 9 / 5 * ftempC + 32
#
# print('Температура по Фаренгейту равна: ', format(tempF, ',.2f'))
# ---------------------------------------------------------------------------------

# need = input('Сколько булочек вы хотите сделать? ')
# needInt = int(need)
#
#                           сахара 0.03, масла 0.02, муки 0.05 - на одну булочку
#
# Sug = needInt * 0.03
# Maslo = needInt * 0.02
# Muka = needInt * 0.05
#
# print('Вам потребуется сахара: ', format(Sug, ',.2f'), '\n'
#       'Вам потребуется масла: ', format(Maslo, ',.2f'), '\n'
#       'Вам потребуется муки: ', format(Muka, ',.2f'))
# -----------------------------------------------------------------------------------

# boys = input('Сколько в классе парней? ')
# boysInt = int(boys)
# girls = input('Сколько в классе девушек? ')
# girlsInt = int(girls)
#
# summ = boysInt + girlsInt
# boysPercent = boysInt / summ
# girlsPercent = girlsInt / summ
#
# print('Учеников в классе: ', summ, '\n'
#       'Процент парней: ', boysPercent, '\n',
#       'Процент девушек: ', girlsPercent)
# ----------------------------------------------------------------------------------------

# STOCK = 2000                        # количество акций
#
# buy = STOCK * 40
# print('Сумма стартового капитала: ', buy)
#
# buyComm = buy * 0.03                # комиссия при покупке 3%
# print('Комиссия покупки 3% =', format(buyComm, ',.2f'))
#
# sell = STOCK * 42.75
# print('Сумма капитала после продажи акций: ', format(sell, ',.2f'))
#
# sellComm = sell * 0.03              # комиссия при продаже 3%
# print('Комиссия продажи 3% =', format(sellComm, ',.2f'))
#
# summComm = buyComm + sellComm
# print('Сумма общей комиссии составила: ', format(summComm, ',.2f'))
#
# profit = sell - summComm
# print('Профит составил: ', format(profit, ',.2f'))
# -------------------------------------------------------------------------------------

# V = кол-во виноградных лоз
# R = длинна грядки в метрах
# E = размер пространства в метрах, занимаемыми концевыми опорами
# S = размер пространства между вин-ми лозами в метрах

# R = input('Введите длину грядки в метрах: ')
# Rint = int(R)
# E = input('Введите объём пространства концевой опоры: ')
# Eint = int(E)
# S = input('Введите объём пространства между лозами в метрах: ')
# Sint = int(S)
#
# V = Rint - (2 * Eint) / Sint
# print('Количество виноградных лоз = ', V)
# ------------------------------------------------------------------------
# A = сумма денег на счёте после количества лет
# P = основной депозит на старте
# r = годовая % ставка
# n = частота начисления %-ого дохода в год
# t = конкретное количество лет

# P = input('Введите основной депозит: ')
# Pint = int(P)
# r = input('Введите годовую % ставку: ')
# rint = int(r)
# n = input('Введите частоту начисления %-ого дохода в год: ')
# nint = int(n)
# t = input('В течении скольки лет вклад будет работать? ')
# tint = int(t)
#
# rStavka = rint / 100                # перевод % ставки в нужный "формат"
# print(rStavka)
#
# A = Pint * (1 + rStavka / nint) ** (nint * tint)
# print('Выходная сумма после', t, 'лет =', format(A, ',.2f'))
# -----------------------------------------------------------------------







