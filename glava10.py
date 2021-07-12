# Глава 8
# - Алгоритмический тренажёр -
#
# class Mycar:
#     def __init__(self):
#         self.__name = 'Roman'
#     def go(self):
#         return self.__name
# mycar = Mycar()
# print(mycar.go())
# --

# class Book:
#     def __init__(self, zagolovok, avtor, izdatel):
#         self.__zag = zagolovok
#         self.__avtor = avtor
#         self.__izd = izdatel
#
#     def set_zag(self, zagolovok):
#         self.__zag = zagolovok
#
#     def set_avtor(self, avtor):
#         self.__avtor = avtor
#
#     def set_izd(self, izdatel):
#         self.__izd = izdatel
#
#     def get_zag(self):
#         return self.__zag
#
#     def get_avtor(self):
#         return self.__avtor
#
#     def get_izd(self):
#         return self.__izd
#
#     def __str__(self):
#         return 'Заголовок книги:' + self.__zag + \
#                '\nИмя автора:' + self.__avtor + \
#                '\nИздательство:' + self.__izd
#
#
# zagolovok = input('zag')
# avtor = input('avtor')
# izdatel = input('izd')
# mybook = Book(zagolovok, avtor, izdatel)
# print(mybook)

# ------------- ЗАДАЧИ ---------------
# 1. класс Pet
#
# class Pet:
#     def __init__(self, name, atype, age):
#         self.__name = name
#         self.__atype = atype
#         self.__age = age
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_type(self, atype):
#         self.__atype = atype
#
#     def set_age(self, age):
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def get_atype(self):
#         return self.__atype
#
#     def get_age(self):
#         return self.__age
#
#
# name = input('Name: ')
# atype = input('Animal type: ')
# age = input('Age: ')
#
# myDog = Pet(name, atype, age)
#
# print('Name:', myDog.get_name(), '\nType:', myDog.get_atype(), '\nAge:', myDog.get_age())
# ---------------------------------------------------------------------------------
# 2. класс Car
#
# class Car:
#     def __init__(self, ymodel, make):
#         self.__year_model = ymodel
#         self.__make = make
#         self.__speed = 0
#
#     def accelerate(self):
#         self.__speed += 5
#
#     def handbreak(self):
#         self.__speed -= 5
#
#     def get_speed(self):
#         return self.__speed
#
#
# ymodel = 1980
# make = 'Audi'
#
# testCar = Car(ymodel, make)
# print('Car testing:', make, '| Year:', ymodel)
# for count in range(5):
#     testCar.accelerate()
#     print('speed:', testCar.get_speed())
#
# print('Finall speed:', testCar.get_speed())
#
# for count in range(5):
#     testCar.handbreak()
#     print('break speed:', testCar.get_speed())
# ---------------------------------------------------------------------------------
# 3. класс персональных данных information
#
# class Info:
#     def __init__(self, name, adress, age, phone):
#         self.__name = name
#         self.__adress = adress
#         self.__age = age
#         self.__phone = phone
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_adress(self, adress):
#         self.__adress = adress
#
#     def set_age(self, age):
#         self.__age = age
#
#     def set_phone(self, phone):
#         self.__phone = phone
#
#     def get_name(self):
#         return self.__name
#
#     def get_adress(self):
#         return self.__adress
#
#     def get_age(self):
#         return self.__age
#
#     def get_phone(self):
#         return self.__phone
#
#
# def main():
#
#     info_list = create()
#     display(info_list)
#
#
# def create():
#     data = []
#
#     for item in range(1, 4):
#         print('Info. about', item, 'guy.')
#         name = input('Name: ')
#         adress = input('Adress: ')
#         age = input('Age: ')
#         phone = input('Phone: ')
#         print()
#         info = Info(name, adress, age, phone)
#         data.append(info)
#     return data
#
#
# def display(info):
#     for item in info:
#         print(item.get_name())
#         print(item.get_adress())
#         print(item.get_age())
#         print(item.get_phone())
#         print()
#
#
# main()
# ---------------------------------------------------------------------------------
# 4. класс Employee [надо было сделать как в 5 задаче, но сделал как в 3.]
#
# class Employee:
#     def __init__(self, name, id, otdel, dolj):
#         self.__name = name
#         self.__id = id
#         self.__otdel = otdel
#         self.__dolj = dolj
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_id(self, id):
#         self.__id = id
#
#     def set_otdel(self, otdel):
#         self.__otdel = otdel
#
#     def set_dolj(self, dolj):
#         self.__dolj = dolj
#
#     def get_name(self):
#         return self.__name
#
#     def get_id(self):
#         return self.__id
#
#     def get_otdel(self):
#         return self.__otdel
#
#     def get_dolj(self):
#         return self.__dolj
#
#
# def main():
#
#     data = create()
#     display(data)
#
#
# def create():
#     data_list = []
#
#     for count in range(1, 4):
#         print('Сотрудник #', count)
#         name = input('Name: ')
#         id = input('id: ')
#         otdel = input('Otdel: ')
#         dolj = input('Doljnost'': ')
#         print()
#         Object = Employee(name, id, otdel, dolj)
#         data_list.append(Object)
#     return data_list
#
#
# def display(data):
#     for item in data:
#         print('Имя:', item.get_name())
#         print('id:', item.get_id())
#         print('Отдел:', item.get_otdel())
#         print('Должность:', item.get_dolj())
#         print()
#
#
# main()
# ---------------------------------------------------------------------------------
# 5 класс Retailitem
#
# class Retailitem:
#     def __init__(self, price, count, about):
#         self.__price = price
#         self.__count = count
#         self.__about = about
#
#     def set_price(self, price):
#         self.__price = price
#
#     def set_count(self, count):
#         self.__count = count
#
#     def set_about(self, about):
#         self.__about = about
#
#     def get_price(self):
#         return self.__price
#
#     def get_count(self):
#         return self.__count
#
#     def get_about(self):
#         return self.__about
#
#
# def main():
#     product1 = Retailitem('59.95', '12', 'Jacket')
#     product2 = Retailitem('34.95', '40', 'Jeans')
#     product3 = Retailitem('24.95', '20', 't-shirt')
#
#     print('Product 1.')
#     print('Price:', product1.get_price())
#     print('Count:', product1.get_count())
#     print('About:', product1.get_about())
#     print()
#     print('Product 2.')
#     print('Price:', product2.get_price())
#     print('Count:', product2.get_count())
#     print('About:', product2.get_about())
#     print()
#     print('Product 3.')
#     print('Price:', product3.get_price())
#     print('Count:', product3.get_count())
#     print('About:', product3.get_about())
#
#
# main()
# ---------------------------------------------------------------------------------
# 6. Расходы на лечение
#
# import Medic
#
# patient = Medic.Patient('Hatkevich Roman Sergeevich', 'Tomsk. obl., Kojev.', '212-199', 'Serega, 911')
#
# procedure1 = Medic.Procedure('Врачебный осмотр', 'сегодня', 'Ирвин А.А', 250)
# procedure2 = Medic.Procedure('Рентгеноскопия', 'сегодня', 'Джемисон Г.Г', 500)
# procedure3 = Medic.Procedure('Анализ крови', 'сегодня', 'Смит У.С', 200)
#
# print('Сведения о пациенте.')
# print('----------------------')
# print('Ф.И.О:', patient.get_fio())
# print('Адрес проживания:', patient.get_adress())
# print('Телефон:', patient.get_phone())
# print('SOS-контакт:', patient.get_sos())
# print()
# print('Сведения о процедурах пациента.')
# print('----------------------')
# print('Процедура №1.')
# print('Название процедуры:', procedure1.get_name())
# print('Дата:', procedure1.get_date())
# print('Врач:', procedure1.get_medic())
# print('Цена:', procedure1.get_price())
# print()
# print('Процедура №2.')
# print('Название процедуры:', procedure2.get_name())
# print('Дата:', procedure2.get_date())
# print('Врач:', procedure2.get_medic())
# print('Цена:', procedure2.get_price())
# print()
# print('Процедура №3.')
# print('Название процедуры:', procedure3.get_name())
# print('Дата:', procedure3.get_date())
# print('Врач:', procedure3.get_medic())
# print('Цена:', procedure3.get_price())
# print()
#
# print('Общая сумма к оплате за процедурные услуги:',
#       procedure1.get_price() + procedure2.get_price() + procedure3.get_price())
# ---------------------------------------------------------------------------------
# 7. Система управления персоналом
#
# import pickle
#
#
# class Employee:
#     def __init__(self, id, name, otdel, dolj):
#         self.__id = id
#         self.__name = name
#         self.__otdel = otdel
#         self.__dolj = dolj
#
#     def set_id(self, id):
#         self.__id = id
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_otdel(self, otdel):
#         self.__otdel = otdel
#
#     def set_dolj(self, dolj):
#         self.__dolj = dolj
#
#     def get_id(self):
#         return self.__id
#
#     def get_name(self):
#         return self.__name
#
#     def get_otdel(self):
#         return self.__otdel
#
#     def get_dolj(self):
#         return self.__dolj
#
#     def __str__(self):
#         return "Имя: %s\nОтдел: %s\nДолжность: %s" % (self.__name, self.__otdel, self.__dolj)
#
#
# FIND = 1
# ADD = 2
# CHANGE = 3
# DEL = 4
# EXIT = 5
#
#
# try:
#     file = open('manage.dat', 'rb')
#     base = pickle.load(file)
#     file.close()
# except FileNotFoundError:
#     base = {}
#
#
# def main():
#     menu()
#
#
# def menu():
#     print()
#     print('Меню.')
#     print('---------')
#     print('1. Найти сотрудника.')
#     print('2. Добавить сотрудника.')
#     print('3. Изменить имя, отдел и должность сотрудника.')
#     print('4. Удалить сотрудника.')
#     print('5. Выйти из программы.')
#     print()
#     choice = int(input('Выберите пункт меню: '))
#     while choice < 1 or choice > 5:
#         choice = int(input('Некорректный выбор, попробуйте снова: '))
#
#     if choice == FIND:
#         find()
#         menu()
#     elif choice == ADD:
#         add()
#         menu()
#     elif choice == CHANGE:
#         change()
#         menu()
#     elif choice == DEL:
#         deleted()
#         menu()
#     elif choice == EXIT:
#         file_dump = open('manage.dat', 'wb')
#         pickle.dump(base, file_dump)
#         file_dump.close()
#         print('Словарь сохранён в manage.dat')
#         exit()
#
#
# def find():
#     user = input('Введите ID сотрудника для поиска: ')
#     if user in base:
#         print('Есть такой.')
#         print(base[user])
#     else:
#         print('Не найдено.')
#
#
# def add():
#     id = input('ID: ')
#     name = input('Имя: ')
#     otdel = input('Отдел: ')
#     dolj = input('Должность:')
#     obj = Employee(id, name, otdel, dolj)
#     base[id] = obj
#
#
# def change():
#     ID = input('ID сотрудника: ')
#     if ID in base:
#         name = input('Имя: ')
#         otdel = input('Отдел: ')
#         dolj = input('Должность:')
#         obj = Employee(ID, name, otdel, dolj)
#         base[ID] = obj
#         print('Info. updated.')
#         print(obj.get_name())
#         print(obj.get_otdel())
#         print(obj.get_dolj())
#     else:
#         print('Такого сотрудника нет.')
#
#
# def deleted():
#     user = input('ID сотрудника: ')
#     if user in base:
#         del base[user]
#         print('Сотрудник удалён.')
#     else:
#         print('Сотрудник не найден.')
#
#
# main()
# --------------------------------------------------------------------------------
# 8. Класс CashRegister
# [В целом понятно что и куда идёт, но затуп на выводе опять, до тотал цены не добрался из за этого]
#
# class Retailitem:
#     def __init__(self, price, count, about):
#         self.__price = price
#         self.__count = count
#         self.__about = about
#
#     def set_price(self, price):
#         self.__price = price
#
#     def set_count(self, count):
#         self.__count = count
#
#     def set_about(self, about):
#         self.__about = about
#
#     def get_price(self):
#         return self.__price
#
#     def get_count(self):
#         return self.__count
#
#     def get_about(self):
#         return self.__about
#
#
# class CashRegister:
#     def __init__(self):
#         self.list_obj = []
#
#     def purchase_item(self, product):
#         self.list_obj.append(product)
#
#     def get_total(self):
#         # total = 0.0
#         # for i in self.list_obj:
#         #     total += i.get_price()
#         pass
#
#     def show_items(self):
#        # return print((str(item) for item in self.list_obj))
#        for item in self.list_obj:
#            # for count in item:
#            print(str(item))
#         # return '%s' % self.list_obj.
#         # pass
#
#     def __repr__(self):
#         return print((str(item) for item in self.list_obj))
#
#     # def __repr__(self):
#     #     return '%s' % Retailitem
#
# def main():
#     product1 = Retailitem('59.95', '12', 'Jacket')
#     product2 = Retailitem('34.95', '40', 'Jeans')
#     product3 = Retailitem('24.95', '20', 't-shirt')
#     obj = CashRegister()
#
#     print('Добро пожаловать в магазин! Выберите товары для покупки.')
#
#     print('Product #1.')
#     print('Price:', product1.get_price())
#     print('Count:', product1.get_count())
#     print('About:', product1.get_about())
#     print()
#     print('Product #2.')
#     print('Price:', product2.get_price())
#     print('Count:', product2.get_count())
#     print('About:', product2.get_about())
#     print()
#     print('Product #3.')
#     print('Price:', product3.get_price())
#     print('Count:', product3.get_count())
#     print('About:', product3.get_about())
#     print()
#
#     print('Введите 0 чтобы выйти из магазина.')
#     choice = int(input('Выберите, что положить в корзину (1,2,3..):'))
#     while choice >= 0 or choice <= 3:
#         if choice == 1:
#             obj.purchase_item(product1)
#             choice = int(input('Что ещё? (1,2,3..):'))
#         elif choice == 2:
#             obj.purchase_item(product2)
#             choice = int(input('Что ещё? (1,2,3..):'))
#         elif choice == 3:
#             obj.purchase_item(product3)
#             choice = int(input('Что ещё? (1,2,3..):'))
#         elif choice == 5:
#             obj.show_items()
#             print(obj)
#             print(repr(obj))
#             print(str(obj.show_items()))
#             print(obj.get_total())
#             break
#         elif choice == 0:
#             print('Спасибо за покупку.')
#             quit()
#         else:
#             print('Товар не существует.')
#             break
#
#
# main()