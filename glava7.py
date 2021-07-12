# Глава 7

# numbers = list(range(3))
# print(numbers)
# size = len(numbers)
# print(size)
# numbers = [1, 2, 3, 4, 5]
# numbers.insert(10, 23)
# # print(numbers)
# # numbers.sort()
# z = numbers.index(5)
# print(z)
# -----------
# - Алгоритмический тренажёр
# -----------
# 1-2.
# names = ['Эйнштейн', 'Ньютон', 'Коперник', 'Кеплер']
# for item in names:
#     print(item)
# ---------
# 3.
# numbers = [0] * 100
# numbers2 = [] + numbers
#
# # numbers2 += numbers
# print(numbers)
# print(numbers2)
# ---------
# 5.
# count = [1, 2, 3, 4, 5]
#
# def get_total(value):
#     total = 0
#     for var in value:
#         total += var
#     return total
# print(get_total(count))
# ---------
# 6.
# names = ['Roman', 'Rybi', 'Vova']
#
# search = input('Кого ищем? ')
#
# if search in names:
#     print('Есь такой фрукт')
# else:
#     print('Net такого тутма')
# ---------
# 8.
# ROWS = 5
# COLS = 3
#
# doublemass = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]        # 3 столбца и 5 строк
#
# for r in range(ROWS):
#     for c in range(COLS):
#         doublemass [r][c] = int(input('Значение: '))
#
# print(doublemass)
# -------------------ЗАДАЧИ--------------------------
#
# 1. Общий объём продаж
#
# DAYS = 7
# total = 0
# sales = []
#
# for day in range(1, DAYS + 1):
#     print('Day №', day)
#     sales.append(int(input('value: ')))
# print(sales)
#
# for x in sales:
#     total += x
#
# print('total value = ', total)
# --------------------------------------------------------------
# 2. Генератор лотерейных чисел
#
# import random
# NUM = 7
#
# lot = []
#
# for count in range(NUM):
#     lot.append(random.randint(0, 9))
#
# for item in lot:
#     print(item)
# --------------------------------------------------------------
# 3. Статистика дождевых осадков
#
# MONTH = 12
#
#
# def main():
#     stat = []
#     for month in range(1, MONTH + 1):
#         print('Месяц №', month)
#         stat.append(int(input('Количество осадков: ')))
#
#     def get_total(val):
#         totall = 0
#         for count in val:
#             totall += count
#         return totall
#
#     total = get_total(stat)
#     print('Общее количество осадков за 12 месяцев:', total)
#     average = total / MONTH
#     print('Среднее ежемесячное количество осадков:', average)
#     print('Мин. осадки:', min(stat), 'Макс. осадки:', max(stat))
#
#
# main()
# --------------------------------------------------------------
# 4. Программа анализа чисел
#
# NUM = 20
# total = 0
# num = []
#
# for x in range(NUM):
#     num.append(int(input('Number: ')))
# for count in num:
#     total += count
# average = total / NUM
#
# print('Общая сумма чисел:', total)
# print('Среднее значение чисел:', average)
# print('Min.', min(num), 'Max.', max(num))
# --------------------------------------------------------------
# 5. Проверка допустимости номера расходного счёта
#
# file = open('accum.txt', 'r')
# list = file.readlines()
#
# search = input('Что ищем? ')
#
# index = 0
# while index < len(list):
#     list[index] = list[index].rstrip('\n')
#     index += 1
#
# if search in list:
#     print('Мы нашли -', search, 'есть в файле!')
# else:
#     print('Мы не нашли такого :(')
#
# file.close()
# --------------------------------------------------------------
# 6. Больше числа n
# spis = [1, 2, 3, 4, 5, 22, 33, 10]
# n = 5
#
#
# def over(spis, n):
#     for count in spis:
#         if count > n:
#             print(count)
#
#
# over(spis, n)
# --------------------------------------------------------------
# 7. Экзамен на получение водит-х прав.
#
# ERROR = 0
# DONE = 0
# index = 0
# indexCheck = 0
# answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
#            'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
#
# ekzfile = open('Ekzamen.txt', 'r')
# ekz = ekzfile.readlines()
#
# while index < len(ekz):
#     ekz[index] = ekz[index].rstrip('\n')
#     index += 1
#
# for count in ekz:
#     if count == answers[indexCheck]:
#         indexCheck += 1
#         DONE += 1
#     else:
#         indexCheck += 1
#         ERROR += 1
#         print('Ошибка в вопросе №:', indexCheck)
#
# print('ИТОГО:', '\nВерных:', DONE, '\nНеверных:', ERROR)
#
# if DONE >= 15:
#     print('Экзамен сдан! Поздравляю!')
# else:
#     print('Вы провалили экзамен. Приходите на пересдачу!')
#
# ekzfile.close()
# --------------------------------------------------------------
# 8. Поиск имени
#
# def main():
#     index = 0
#     boyName = False
#     girlName = False
#
#     boys = open('boys.txt', 'r')
#     girls = open('girls.txt', 'r')
#
#     boys_list = boys.readlines()
#     girls_list = girls.readlines()
#
#     while index < len(boys_list and girls_list):
#         boys_list[index] = boys_list[index].rstrip('\n')
#         girls_list[index] = girls_list[index].rstrip('\n')
#         index += 1
#
#     user_boy = input('Имя мальчика: ')
#     user_girl = input('Имя девочки: ')
#     # Поиск имени в списке мальчиков
#     for count in boys_list:
#         if count == user_boy:
#             boyName = True
#     # Поиск имени в списке девочек
#     for count in girls_list:
#         if count == user_girl:
#             girlName = True
#
#     if boyName:
#         print('Имя мальчика в списке')
#     else:
#         print('Имя мальчика не в списке')
#
#     if girlName:
#         print('Имя девушки в списке')
#     else:
#         print('Имя девушки не в списке')
#
#
# main()
# --------------------------------------------------------------
# 9. Данные о населении
# --- Создал файл для задачи---
# import random
#
# file = open('USA.txt', 'w')
#
# for count in range(40):
#      file.write(str(random.randint(1000, 8000)) + '\n')
#
# file.close()
# -------------- Сама Задача[НЕ ДОДЕЛАНА] ------------
# Year = 1950
# DelN = 0
# print('Данные о населении USA с 1950 по 1990 года.\n')
# data = open('USA.txt', 'r')
# data_list = data.readlines()
#
# fromYear = input('С какого года? ')
# toYear = input('По какой год? ')
#
# while DelN < len(data_list):
#     data_list[DelN] = data_list[DelN].rstrip('\n')
#     DelN += 1
#     # Year += 1
#
# srez = data_list[30:]
#
# for count in srez:
#     print(count)
# # print(DelN)
# # print(Year)
# ------------------------------------------------------
# 10. Чемпионы мировой серии
# delN = 0
# Years = 0
# file = open('WorldSeriesWinners.txt', 'r')
# file_list = file.readlines()
# file.close()
# while delN < len(file_list):
#     file_list[delN] = file_list[delN].rstrip('\n')
#     delN += 1
#
# user = input('Team name: ')
#
# for count in file_list:
#     if user == count:
#         Years += 1
# print('Команда', user, 'побеждала в Мировой серии', Years, 'раз(а)!')
# ------------------------------------------------------
# 11. Магический квадрат Ло Шу[я незнаю, забил]
#
# RAWS = 3
# COLS = 3
# z = 0
# quad = [[4, 9, 2],
#         [3, 5, 7],
#         [8, 1, 6]]
# # for r in range(RAWS):
# #     for c in range(COLS):
# #         print('Magic')
# print(quad[2][2])
# if quad[0][0] + quad[0][1] + quad[0][2] == quad[1][0] + quad[1][1] + quad[1][2] \
#    == quad[2][0] + quad[2][1] + quad[2][2] == [0][0] + quad[1][1] + quad[2][2] \
#    == quad[0][1] + quad[1][1] + quad[2][1] == [0][0] + quad[1][0] + quad[2][0] \
#    == quad[0][2] + quad[1][2] + quad[2][2] == quad[2][0] + quad[1][1] + quad[0][2]:
#     print('Magic here lol')
# else:
#     print('Error')
# print(quad)
# ------------------------------------------------------
# ------------------------------------------------------
# 13. Волшебный шар
#
# import random
# index = 0
# file = open('8_ball.txt', 'r')
# file_list = file.readlines()
# file.close()
#
# while index < len(file_list):
#     file_list[index] = file_list[index].rstrip('\n')
#     index += 1
#
# go = 'д'
#
# while go == 'д':
#     quest = input('Спроси меня: ')
#     file_list_answer = random.randrange(len(file_list))
#     print(file_list[file_list_answer])
#     go = input('Спросить ещё раз?(д/н): ')
# else:
#     print('Пока')
# ------------------------------------------------------
# 14. Круговая диаграмма расходов
#
# import matplotlib.pyplot as plt
# indx = 0
# file = open('MyZatratPie.txt', 'r')
# file_list = file.readlines()
# while indx < len(file_list):
#     file_list[indx] = file_list[indx].rstrip('\n')
#     indx += 1
# file.close()
# names = ['pivo', 'samogonka', 'vodka', 'PC games', 'music', 'games xbox']
#
# plt.pie(file_list, labels=names)
# plt.title('Мои затраты за месяц')
# plt.show()
# ------------------------------------------------------
# 15. График еженедельных цен на бензин за 1994 год
# - создал файл для задачи -
# import random
# file = open('Gas.txt', 'w')
#
# for c in range(52):
#     file.write(str(random.randint(30, 60)) + '\n')
# file.close()
# ------- задача ---------
#
# import matplotlib.pyplot as plt
# indx = 0
# file = open('Gas.txt', 'r')
# file_list = file.readlines()
#
# while indx < len(file_list):
#     file_list[indx] = file_list[indx].rstrip('\n')
#     indx += 1
#
# file_list.sort()
#
# plt.title('Цена на бензин за 1994 год')
# plt.plot(file_list)
# plt.grid(True)
# plt.xlabel('Недели')
# plt.ylabel('Цена')
# plt.xlim(xmin=0, xmax=52)
# plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
#             16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
#             31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
#            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
#             '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
#             '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45',
#             '46', '47', '48', '49', '50', '51', '52'])
