# Глава 8
#
# mystring = 'domashka'
# if 'd' in mystring:
#     print('+')
# else:
#     print('-')
# -----------------------
# #
# big = 'NANDO YO'
# litttle = big.lower()
# print(litttle)
# -----------------------
#
# chislo = '12322a'
# if chislo.isdigit():
#     print('Number')
# else:
#     print('Note number')
# -----------------------
#
# g = 'g'
#
# while g.lower() == 'g':
#     g = input('Eshe raz sprosit(g/n): ')
# # -----------------------
# var = '$'
# print(var.upper())
# ----------------------
# n = 0
# mystring = 'AAaaAAaaAAaaAA'
#
# for c in mystring:
#     if c.isupper():
#         n += 1
# print(n, 'букв в верхнем регистре')
# ----------------------
# days = 'Пн Вт Ср'
# print(days.split())
# days = 'Пн#Вт#Ср#Чт'
# print(days.split('#'))
# ---- Алгоритмический тренажёр -----------
# choice = 'vovan228' # [кал какой то]
# if choice.lower() == '11':
#     print('lol')
# else:
#     print('no')
# ---------------------
# n = 0
# mystring = 'vova vova vovanchik'
# for count in mystring:
#     if count.isspace():
#         n += 1
# print(n, 'probels')
# n = 0
# mystring = 'vova vova vovanchik228'
# for count in mystring:
#     if count.isdigit():
#         n += 1
# print(n, 'цифры')
# n = 0
# mystring = 'vova vova VAVANCHik228'
# for count in mystring:
#     if count.islower():
#         n += 1
# print(n, 'цифры')
# -------------------------------------
#
# user = input('name: ')
#
# def check(user):
#     if user.endswith('.com'):
#         return True
#
# if check(user):
#     print('True .com')
# else:
#     print('Note .com')
# -------------------------------------
# string = 'nnnaASssdnnDD'
# print(string.replace('n', 'N'))
# -------------------------------------
# string = '1 2 3 4 5'
# def reverse(string):
#     for i in range(-1, -len(string) - 1, -1):
#         print(string[i], end=(""))
# reverse(string)
# -------------------------------------
# string = 'vovanGamer777'
# print(string[0:3])
# string = 'vovanGamer777'
# print(string[-3:])
# -------------------------------------
# string = 'пироги<баклажаны<вода<водочка<водичка'
# print(string.split('<'))
# -------------------- ЗАДАЧИ ПОШЛИ -------------------------
# 1. Инициалы
#
# first = input('Name: ')
# last = input('Familiya: ')
# midle = input('Otchestvo: ')
#
# print('Инициалы:')
# print(first[:1], last[:1], midle[:1] + '.', sep='.')
# ----------------------------------------------
# 2. Сумма цифр в строке
#
# t = 0
# user = input('numbers: ')
# for count in user:
#     t += int(count)
# print(t, 'sum')
# ----------------------------------------------
# 3. Принтер дат
#
# from datetime import datetime
# date_input = input('Enter a date(mm/dd/yyyy): ')
# date_object = datetime.strptime(date_input, '%m/%d/%Y')
# print(date_object.strftime('%B %d, %Y'))
# ----------------------------------------------
# 4. Конвертер азбуки Морзе
#
# В целом, сразу понял, что нужно сделать кучу if-elif и гонять по while-циклу каждое значение.
# Если бы посидел ещё минут 30, то думаю исправил бы пару ошибок и написал в нужной последовательности, скажем так.
# Но, писать столько ифов, верил, что есть ещё способ. Этот способ мне понравился больше + тут ещё и звуки.
#
# import winsound
# import time
#
# # Принимаем из Russian_to_Morse для очистки, всё в нижний регистр + что-то с юникод-кодом.
# # Я думаю, мы ставим диапазон допустимых символов(буквы), а остальное просто не записывается и не возвращается.
# def Clean_stroke(content):
#     result = []
#     content = str(content).lower()
#
#     for element in content:
#         if ord(element) >= 1072 and ord(element) <= 1103:
#             result.append(element)
#
#     return result
#
# # Принимаем введённое user'ом строковое значение, передаём его в Clean_stroke.
# def Russian_to_Morse(content):
#     rus_to_morse = {'а': '.-',
#                     'б': '-...',
#                     'в': '.--',
#                     'г': '--.',
#                     'д': '-..',
#                     'е': '.',
#                     'ж': '...-',
#                     'з': '--..',
#                     'и': '..',
#                     'й': '.---',
#                     'к': '-.-',
#                     'л': '.-..',
#                     'м': '--',
#                     'н': '-.',
#                     'о': '---',
#                     'п': '.--.',
#                     'р': '.-.',
#                     'с': '...',
#                     'т': '-',
#                     'у': '..-',
#                     'ф': '..-.',
#                     'х': '....',
#                     'ц': '-.-.',
#                     'ч': '---.',
#                     'ш': '----',
#                     'щ': '--.-',
#                     'ъ': '.--.-.',
#                     'ы': '-.--',
#                     'ь': '-..-',
#                     'э': '..-..',
#                     'ю': '..--',
#                     'я': '.-.-'}
#
#     content = Clean_stroke(content)
#     result = []
# # Получили обратно фильтрованные данные и прогоняя каждый элемент, записали их значения в список и вернули.
#     for element in content:
#         result.append(rus_to_morse[element])
#
#     return result
#
# #
# frequency = 1000
# content = Russian_to_Morse(input('Введите слово:'))
# print(content)
# # Часть озвучки символов, на глаз примерно понятно как работает.))
# for set in content:
#     for symbol in set:
#         if symbol == '.':
#             winsound.Beep(frequency, 100)
#         elif symbol == '-':
#             winsound.Beep(frequency, 700)
#     print()
#     time.sleep(0.2)                                     # значение паузы между звуками ("словами").
#
# ---------------------------------------------------------------------------------------
# 5. Алфавитный переводчик номера телефона. Я СМОГ ))
#
# def phone_code(number):
#     code_list = {'a': '2', 'b': '2', 'c': '2',
#                  'd': '3', 'e': '3', 'f': '3',
#                  'g': '4', 'h': '4', 'i': '4',
#                  'j': '5', 'k': '5', 'l': '5',
#                  'm': '6', 'n': '6', 'o': '6',
#                  'p': '7', 'q': '7', 'r': '7', 's': '7',
#                  't': '8', 'u': '8', 'v': '8',
#                  'w': '9', 'x': '9', 'y': '9', 'z': '9',
#                  '1': '1',
#                  '2': '2',
#                  '3': '3',
#                  '4': '4',
#                  '5': '5',
#                  '6': '6',
#                  '7': '7',
#                  '8': '8',
#                  '9': '9',
#                  '0': '0',
#                  '-': '-'}
#     number_list = []
#     for count in number:
#        number_list.append(code_list[count])
#     return number_list
#
#
# number = phone_code(str(input('Введите номер телефона(Enter-выход): ').lower()))
# print('Номер вашей доставки: ', end='')
# for c in number:
#     print(c, end='')
# ---------------------------------------------------------------------------------------
# 6. Среднее количество слов
#
# delN = 0
# counter = 0
# file = open('text.txt', 'r')
# file_list = file.readlines()
# file.close()
# while delN < len(file_list):
#     file_list[delN] = file_list[delN].rstrip('\n')
#     delN += 1
#
# for c in range(delN):
#     x = (file_list[c].split())
#     print('Предложение №', c+1, ': ', len(x), sep='')
#     for count in x:
#         counter += 1
#
# average = counter / delN
# print('Предложений:', delN, '\nВсего слов:', counter, '\nСреднее количество слов:', average)
# ---------------------------------------------------------------------------------------
# 7. Анализ символов
#
# delN = 0
# lower = 0
# upper = 0
# space = 0
# digit = 0
#
# file = open('text.txt', 'r')
# list = file.readlines()
# file.close()
# while delN < len(list):
#     list[delN] = list[delN].rstrip('\n')
#     delN += 1
#
# for c in range(delN):
#     x = (list[c].split())
#     for cc in x:
#         cc.isspace()
#         space += 1
#         for count in cc:
#             if count.islower():
#                 lower += 1
#             elif count.isupper():
#                 upper += 1
#             elif count.isdigit():
#                 digit += 1
# print(lower, 'букв(ы) в нижнем регистре.')
# print(upper, 'букв(ы) в верхнем регистре.')
# print(space - delN - 1, 'чистых пробела(ов), переносы строк не учитаны.')
# print(digit, 'цифр(ы).')
# ---------------------------------------------------------------------------------------
# 8. Корректор предложений
#
# def corrector(user):
#     return user[0].upper() + user[1:]
# user = input('Vvedite: ')
# print(corrector(user))
# ---------------------------------------------------------------------------------------
# 9. Гласные и согласные
#
# def checker(user):
#     glasnCount = 0
#     soglasnCount = 0
#     glasnoe = ['а', 'у', 'о', 'и', 'э', 'ы', 'я', 'ю', 'е', 'ё']
#     soglasn = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
#     for count in user:
#         if count.isalpha():
#             if count.lower() in glasnoe:
#                 glasnCount += 1
#             elif count.lower() in soglasn:
#                 soglasnCount += 1
#     return print('Согласные:', soglasnCount, 'Гласные:', glasnCount)
#
# user = input('Ввод: ')
# checker(user)
# ---------------------------------------------------------------------------------------
# 10. Самый частотный символ/ Загуглил и судя по всему лучший способ такой.
#
# from collections import Counter
# print(Counter(input('Введите строку: ')).most_common(1))
# ---------------------------------------------------------------------------------------
# 11. Разделитель слов
#
# user = input('Введи строку: ')
# list = []
# for count in user:
#     if count.isupper():
#         list.append(' ')
#         list.append(count.lower())
#     else:
#         list.append(count)
# stri = ''.join(list)
# z = stri[1].upper()
#
# print(list)
# print(z + stri[2:].lstrip())
# ---------------------------------------------------------------------------------------
# 12. Молодёжный жаргон
# [из инета решение(сам split не там делал и затупил).]
# -------
# text = input('Enter: ').lower()
# new_text = ' '.join(word[1:] + word[0] + 'ки' for word in text.split())
# print(new_text)
# ---------------------------------------------------------------------------------------
