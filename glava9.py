# Глава 9

# lib = {'старт':1472,
#        'стsарт':1472,'стаdрт':1472}
# # k = 'key'
# # v = 'sskey'
#
# for k, v in lib:
#     print(k,v)
#
# mys = set([1, 2, 3])
# mss = set([2, 3, 4])
# msss = mys.symmetric_difference(mss)
# print(msss)
#
# --------------------- Алгоритмический тренажёр ----------------------
#
# slovar = {}
# print(slovar)
# slov = {'a': 1,
#         'б': 2,
#         'в': 3,
#         'Джеймс': 10,
#         'Джим': 40}
#
# if 'Джеймс' in slov:
#     print('Он тут! Его очки =', slov.get('Джеймс'))
# else:
#     print('Нету.')
# print(slov)
# if 'Джим' in slov:
#     del slov['Джим']
#     print('Джим был найден и удалён из словаря.')
# else:
#     print('Нету')
# print(slov)
# ------------------множества----------------
# myset1 = set(['10', '20'])
# myset2 = set(['1', '2', '30'])
# myset3 = myset1.union(myset2)
# print(myset3)
# myset1 = set(['1', '20'])
# myset2 = set(['1', '2', '30'])
# myset3 = myset1.intersection(myset2)
# print(myset3)
# myset1 = set(['1', '20'])
# myset2 = set(['1', '2', '30'])
# myset3 = myset1.difference(myset2)
# print(myset3)
# myset1 = set(['1', '20'])
# myset2 = set(['1', '2', '30'])
# myset3 = myset2.difference(myset1)
# print(myset3)
# myset1 = set(['1', '20'])
# myset2 = set(['1', '2', '30'])
# myset3 = myset1.symmetric_difference(myset2)
# print(myset3)
# ---------------------------------------------------
# import pickle
# dct = {'a': 1,
#        'b': 2}
#
# file = open('mydata.dat', 'wb')
# pickle.dump(dct, file)
# file.close()
#
# file_read = open('mydata.dat', 'rb')
# x = pickle.load(file_read)
# file_read.close()
# print(x)
# --------------------------------ЗАДАЧИ-------------------------------------
#
# 1. Информация об учебных курсах
#
# kabinet = {'CS101': 3004, 'CS102': 4501, 'CS103': 6755, 'CS104': 1244, 'CS105': 1411}
# predodn = {'CS101': 'Хайнс', 'CS102': 'Альварадо', 'CS103': 'Рич', 'NT110': 'Берк', 'CM241': 'Ли'}
# time = {'CS101': '8:00', 'CS102': '9:00', 'CS103': '10:00', 'NT110': '11:00', 'CM241': '13:00'}
#
# user = input('Номер курса: ')
#
# if user in kabinet:
#     print('Аудитория №', kabinet[user])
# else:
#     print('Аудитория не назначена.')
# if user in predodn:
#     print('Преподаватель:', predodn[user])
# else:
#     print('Нет преподавателя.')
# if user in time:
#     print('Время лекции:', time[user])
# else:
#     print('Время не назначено.')
# ------------------------------------------------------------------
# 2. Викторина
#
# import random
# verno = 0
# neverno = 0
#
# questions = {'Австрия': 'Вена', 'Албания': 'Тирана', 'Алжир': 'Алжир',
#              'Армения': 'Ереван', 'Афганистан': 'Кабул', 'Беларусь': 'Минск',
#              'Бельгия': 'Брюссель', 'Россия': 'Москва', 'Германия': 'Берлин'}
#
# play = 'д'
# print('Викторина.')
#
# while play == 'д':
#     print('Назовите столицу этой страны:', random.choice(list(questions.keys())))
#     answer = input('Ответ: ')
#     if answer not in questions.values():
#         neverno += 1
#         play = input('Неверно! Хотите сыграть ещё раз?(д/н): ')
#     else:
#         verno += 1
#         play = input('Верно! Хотите сыграть ещё раз?(д/н): ')
# else:
#     print('Пока-пока!')
#
# print('Правильных ответов:', verno, 'Неправильных ответов:', neverno)
# ------------------------------------------------------------------
#
# 3. Шифрование и дешифрование файлов
# - ввод шифрованных данных.
# codes = {'a': '!',
#          'b': '@',
#          'c': '#',
#          'd': '$',
#          'e': '%',
#          'f': '^',
#          'g': '&',
#          'h': '}',
#          'i': '(',
#          'j': ')',
#          'k': '1',
#          'l': '2',
#          'm': '3',
#          'n': '4',
#          'o': '5',
#          'p': '6',
#          'q': '7',
#          'r': '8',
#          's': '9',
#          't': '0',
#          'u': '+',
#          'v': '-',
#          'w': '/',
#          'x': ']',
#          'y': '[',
#          'z': '.',
#          ' ': ' '}
#
# file = open('codes.txt', 'r')
# file_string = file.readline()
# file.close()
# print(file_string)
#
# file_crypt = open('crypto.txt', 'w')
# for coint in file_string:
#     if coint in codes:
#         file_crypt.write(codes[coint])
# file_crypt.close()
# - программа вывода, дешифрованные данные из файла.
# codes2 = {'!': 'a',
#          '@': 'b',
#          '#': 'c',
#          '$': 'd',
#          '%': 'e',
#          '^': 'f',
#          '&': 'g',
#          '}': 'h',
#          '(': 'i',
#          ')': 'j',
#          '1': 'k',
#          '2': 'l',
#          '3': 'm',
#          '4': 'n',
#          '5': 'o',
#          '6': 'p',
#          '7': 'q',
#          '8': 'r',
#          '9': 's',
#          '0': 't',
#          '+': 'u',
#          '-': 'v',
#          '/': 'w',
#          ']': 'x',
#          '[': 'y',
#          '.': 'z',
#          ' ': ' '}
#
# crypt_file = open('crypto.txt', 'r')
# crypt_line = crypt_file.readline()
# crypt_file.close()
#
# for count in crypt_line:
#     if count in codes2:
#         print(codes2[count], end='')
# ------------------------------------------------------------------
## 4. Уникальные слова
#
# i = 0
# file = open('set.txt', 'r')
# x = file.readlines()
# file.close()
# while i < len(x):
#     x[i] = x[i].rstrip('\n')
#     i += 1
# myset = set(x)
# print(myset)
# ------------------------------------------------------------------
# 5. Частотность слов
#
# i = 0
# file = open('set.txt', 'r')
# file_read = file.readlines()
# file.close()
#
# while i < len(file_read):
#     file_read[i] = file_read[i].rstrip('\n')
#     i += 1
# book = {}
#
# for count in file_read:
#     if count not in book:
#         print(count)
#         book[count] = 1
#     else:
#         book[count] += 1
# print(book)
# ------------------------------------------------------------------
# 6. Анализ файла
#
# file_set = open('set.txt', 'r')
# file_set2 = open('set2.txt', 'r')
#
# set1 = set(file_set)
# set2 = set(file_set2)
# file_set.close()
# file_set2.close()
# # --union - уникальные слова в обоих файлах.
# set3 = set1.union(set2)
# print(set3)
# # --intersection - слова, которые есть в обоих файлах.
# set4 = set1.intersection(set2)
# print(set4)
# # --difference - слова, которые есть в первом файле, но нет во втором.
# set5 = set1.difference(set2)
# print(set5)
# # --difference - слова, которые есть во втором файле, но нет в первом.
# set6 = set2.difference(set1)
# print(set6)
# # --symmetric_difference - слова, которые есть либо в первом, либо во втором, но не входящие в оба файла одновременно.
# set7 = set1.symmetric_difference(set2)
# print(set7)
# ------------------------------------------------------------------
# 7. Победители Мировой серии
# i = 0
# year = 1903
# winCount = {}
# winYears = {}
# file = open('WorldSeriesWinners.txt', 'r')
# file_list = file.readlines()
# file.close()
#
# while i < len(file_list):
#     file_list[i] = file_list[i].rstrip('\n')
#     i += 1
#
# for count in file_list:
#     if count not in winCount:
#         winCount[count] = 1
#     else:
#         winCount[count] += 1
#     winYears[year] = count
#     year += 1
#
# user = int(input('Введите год(между 1903-2007): '))
# while user < 1903 or user > 2007:
#     user = int(input('Неверная дата, введите снова(1903-2007): '))
#
# if user in winYears and winYears:
#     x = winYears[user]
#     print(x, ', побед в Мировой серии:', winCount[x])
# ------------------------------------------------------------------
# 8. Имена и адреса e-mail
#
# def main():
#     import pickle
#     based = {}
#
#     file_read = open('Myemails.dat', 'rb')
#     based = pickle.load(file_read)
#     file_read.close()
#
#     def menu():
#         print('\nМеню.')
#         print('0 - Выйти из программы.',
#               '\n1 - Найти e-mail.',
#               '\n2 - Добавить новое имя и e-mail.',
#               '\n3 - Изменить существующий e-mail.',
#               '\n4 - Удалить существующий e-mail и имя.',
#               '\n5 - Показать словарь.')
#
#         choice_menu = int(input('\nВыберите пункт меню для продолжения: '))
#         while choice_menu < 0 or choice_menu > 6:
#             choice_menu = int(input('Выберите существующий пункт из списка: '))
#
#         if choice_menu == 0:
#             file = open('Myemails.dat', 'wb')
#             pickle.dump(based, file)
#             file.close()
#             print('Словарь законсервирован в файл Myemails.dat')
#             exit()
#         if choice_menu == 1:
#             find_email()
#             menu()
#         if choice_menu == 2:
#             add_new()
#             print('В словарь добавлена новая запись.')
#             menu()
#         if choice_menu == 3:
#             edit()
#             print('Изменение выполнено.')
#             menu()
#         if choice_menu == 4:
#             deleted()
#             print('Успешно удалено.')
#             menu()
#         if choice_menu == 5:
#             print(based)
#             menu()
#
#     def find_email():
#         try:
#             print('Поиск e-mail по имени.')
#             name = input('Имя: ').lower()
#             print('e-mail:', based[name])
#         except:
#             print('Не найдено.')
#
#     def add_new():
#         print('Добавление нового имени и e-mail.')
#         name = input('Имя: ').lower()
#         email = input('email: ')
#         based[name] = email
#
#     def edit():
#         print('Изменение e-mail.')
#         name = input('Чей e-mail будем менять? ').lower()
#         new_mail = input('Новый e-mail: ')
#         based[name] = new_mail
#
#     def deleted():
#         print('Удаление из словаря.')
#         name = input('Кого удаляем?(Имя): ').lower()
#         del based[name]
#
#     menu()
#
#
# main()
# ------------------------------------------------------------------
# 9. Имитация игры в блек-джек[не доделал]
#
import random

# def main():
#     # player1 = 0
#     # player2 = 0
#     deck = create_deck()
#
#     # if player1 or player2 <= 21:
#     # player1 = deal_card_one(deck)
#     player2 = deal_card_two(deck)
#     # print(player1)
#     print(player2)
#     # if player1 and player2 == 21:
#     #     print('Ничья! Оба игрока выбили 21!')
#     # if player2 < player1 <= 21:
#     #     print('Победил player1!')
#     #     print('Счёт:\np1:', player1, '\np2:', player2)
#     # if player1 < player2 <= 21:
#     #     print('Победил player2!')
#     #     print('Счёт:\np1:', player1, '\np2:', player2)
#
#
# def create_deck():
#     deck = {'Туз пик': 1, '2 пик': 2, '3 пик': 3,
#             '4 пик': 4, '5 пик': 5, '6 пик': 6,
#             '7 пик': 7, '8 пик': 8, '9 пик': 9,
#             '10 пик': 10, 'валет пик': 10, 'дама пик': 10, 'король пик': 10,
#
#             'Туз червей': 1, '2 червей': 2, '3 червей': 3,
#             '4 червей': 4, '5 червей': 5, '6 червей': 6,
#             '7 червей': 7, '8 червей': 8, '9 червей': 9,
#             '10 червей': 10, 'валет червей': 10, 'дама червей': 10, 'король червей': 10,
#
#             'Туз треф': 1, '2 треф': 2, '3 треф': 3,
#             '4 треф': 4, '5 треф': 5, '6 треф': 6,
#             '7 треф': 7, '8 треф': 8, '9 треф': 9,
#             '10 треф': 10, 'валет треф': 10, 'дама треф': 10, 'король треф': 10,
#
#             'Туз бубей': 1, '2 бубей': 2, '3 бубей': 3,
#             '4 бубей': 4, '5 бубей': 5, '6 бубей': 6,
#             '7 бубей': 7, '8 бубей': 8, '9 бубей': 9,
#             '10 бубей': 10, 'валет бубей': 10, 'дама бубей': 10, 'король бубей': 10}
#     return deck
#
#
# def deal_card_one(deck):
#     hand_value = 0
#     # number = len(deck)
#     while hand_value <= 21:
#     # for count in range(number):
#         card, value = deck.popitem()
#         print(card)
#         hand_value += value
#         print(hand_value)
#     # print('Величина карт на руках игрока 1:', hand_value)
#     return hand_value
#
#
# def deal_card_two(deck):
#     hand_value = 0
#     # number = len(deck)
#     while hand_value <= 31:
#     # for count in range(number):
#         card, value = deck.popitem()
#         print(card)
#         hand_value += value
#     else:
#         # hand_value > 21:
#         return hand_value
#     # print('Величина карт на руках игрока 2:', hand_value)
#
#
# main()
