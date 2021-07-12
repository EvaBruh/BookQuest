# Глава 6
#
# file = open('files.txt', 'w')
#
# for count in range(1, 11):
#     file.write(str(count) + '\n')
#
# print('Записано в files.txt')
# file.close()
# # ------------------------
# file = open('files.txt', 'r')
#
# read = file.readline()
# read = read.rstrip('\n')
# while read != '':
#     print(read)
#     read = file.readline()
#     read = read.rstrip('\n')
# file.close()
# ------------------------
# file = open('files.txt', 'r')
#
# for count in file:
#     print(count.rstrip('\n'))
#
# file.close()
# ------------------------------------------
# Алгоритмический тренажёр
#
# file = open('my_name.txt', 'w')
# file.write('Roman' + '\n')
# file.close()
# ---------------
# file = open('my_name.txt', 'r')
# print(file.read())
# file.close()
# ---------------
# file = open('number_list.txt', 'w')
# for count in range(1, 100):
#     file.write(str(count) + '\n')
# file.close()
# ---------------
# file = open('number_list.txt', 'r')
# for count in file:
#     print(count.rstrip('\n'))
# file.close()
# ---------------
# total = 0
# file = open('number_list.txt', 'r')
# for count in file:
#     total += int(count)
# print(total)
# file.close()
# ---------------
# file = open('test.txt', 'w')
# file.write('Гуль')
# file.close()
# file = open('test.txt', 'a')
# file.close()
# ---------------создание записей в файле--------
# file = open('students.txt', 'w')
#
# count = int(input('Сколько учеников? '))
# for i in range(1, count + 1):
#     print('Ученик №', i)
#     name = input('Имя: ')
#     ball = input('Оценка: ')
#     file.write(name + '\n')
#     file.write(ball + '\n')
# file.close()
# ----------ИЗМЕНЕНИЕ ЗАПИСИ------------
# import os
#
# found = False
#
# search = input('Кого найти? ')
# new_count = input('Новая оценка: ')
#
# file = open('students.txt', 'r')
# file_new = open('temp.txt', 'w')
#
# exchge = file.readline()
#
# while exchge != '':
#     ball = file.readline()
#     ball = ball.rstrip('\n')
#     exchge = exchge.rstrip('\n')
#     if search == exchge:
#         file_new.write(exchge + '\n')
#         file_new.write(str(new_count) + '\n')
#         found = True
#     else:
#         file_new.write(exchge + '\n')
#         file_new.write(str(ball) + '\n')
#     exchge = file.readline()
#
# file.close()
# file_new.close()
# os.remove('students.txt')
# os.rename('temp.txt', 'students.txt')
#
# if found:
#     print('Update!')
# else:
#     print('Not found')
# ----------УДАЛЕНИЕ ЗАПИСИ------------
# import os
#
# found = False
#
# search = input('Что ищем? ')
# file = open('students.txt', 'r')
# file_new = open('temp.txt', 'w')
#
# descr = file.readline()
#
# while descr != '':
#     ball = file.readline()
#     descr = descr.rstrip('\n')
#     ball = ball.rstrip('\n')
#     if descr != search:
#         file_new.write(descr + '\n')
#         file_new.write(str(ball) + '\n')
#     else:
#         found = True
#
#     descr = file.readline()
#
# file.close()
# file_new.close()
# os.remove('students.txt')
# os.rename('temp.txt', 'students.txt')
#
# if found:
#     print('Update done!')
# else:
#     print('Not found.')
# ------------------------------------------------
# --------ЗАДАЧИ----------------
# 1. Вывод файла на экран
#
# file = open('numbers.txt', 'r')
# x = file.read()
# print(x)
# file.close()
# ------------------------------------------------
# 2-3. Вывод на экран верхней части файла + нумерация. Верхние строки так и не вывел толком, хз.
# 4. Счётчик значений тоже здесь реализованна, в виде накопительной count.

# filename = input('File name: ')
# count = 1
# file = open(filename, 'r')
#
# lines = file.readline()
# lines = lines.rstrip('\n')
# print('Номер строки ', count, ': ', lines, sep='')
#
# while lines != '':
#     lines = file.readline()
#     lines = lines.rstrip('\n')
#     count += 1
#
#     print('Номер строки ', count, ': ', lines, sep='')
#     lines = lines.rstrip('\n')
#
# file.close()
# ------------------------------------------------
# 5 Счётчик значений.

# file = open('numbers.txt', 'r')
# total = 0
#
# for count in file:
#     total += int(count)
#
# print(total)
# file.close()
# ------------------------------------------------
# 6. Среднее арифметическое чисел.

# file = open('numbers.txt', 'r')
# total = 0
# num = 0
#
# for count in file:
#     total += int(count)
#     num += 1
#
# print('Количество строк:', num)
# print('Сумма чисел:', total)
# x = total / num
# print('Среднее:', x)
#
# file.close()
# ------------------------------------------------
# 7. Программа записи файла со случайными числами
#
# import random
#
# file = open('random.txt', 'w')
#
# user = int(input('Сколько чисел ввести? '))
#
# for count in range(1, user):
#     file.write(str(random.randint(1, 500)) + '\n')
# file.close()
# ------------------------------------------------
# 8. Программа чтения файлов со случайными числами
#
# file = open('random.txt', 'r')
# total = 0
# num = 0
#
# for count in file:
#     total += int(count)
#     num += 1
#     print(count.rstrip('\n'))
#
# print('Количество чисел:', num)
# print('Сумма чисел:', total)
#
# file.close()
# ------------------------------------------------
# 9. Обработка исключений
#
# total = 0
# num = 0
#
# file = open('numbers.txt', 'r')
# try:
#
#     for count in file:
#         try:
#             total += int(count)
#         except ValueError:
#             print('Ошибка! тип данных не верный')
#         num += 1
#
#     print('Количество строк:', num)
#     print('Сумма чисел:', total)
#     x = total / num
#     print('Среднее:', x)
# except IOError:
#     print('Ошибка ввода данных')
# file.close()
# ------------------------------------------------
# 10. Гольф
#
### записываем в файл ###
# file = open('golf.txt', 'w')
#
# countPlayers = int(input('Сколько игроков? '))
#
# for ladder in range(1, countPlayers+1):
#     print('Player №:', ladder)
#     player = input('Player name: ')
#     score = input('Score: ')
#     file.write(player + '\n')
#     file.write(score + '\n')
#
# file.close()
# ### читаем файл ###
# readfile = open('golf.txt', 'r')
#
# for count in readfile:
#     print(count.rstrip('\n'))
#
# file.close()
# ------------------------------------------------
# 11. Генератор персональной веб страницы.(lol)
#
# file = open('generator.html', 'w')
#
# name = input('Name: ')
# opisanie = input('About you: ')
#
# file.write('<html>\n<head>\n</head>\n<body>\n <center>\n <h1>' + name + '</h1>\n'
#            ' </center>\n <hr>\n ' + opisanie + '\n </hr>\n</body>\n</html>')
#
# file.close()
# ------------------------------------------------



