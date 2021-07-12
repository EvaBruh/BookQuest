# Глава 11
#
# class Auto:
#     def __init__(self, make, price):
#         self.__make = make
#         self.__price = price
#
#
# class Car(Auto):
#     def __init__(self, make, price, door):
#         Auto.__init__(self, make, price)
#         self.__door = door
#
# class Vegetable:
#     def __init__(self, vegtype):
#         self.__vegtype = vegtype
#
#     def message(self):
#         print('Ovosh')
#
#
# class Potato(Vegetable):
#     def __init__(self):
#         Vegetable.__init__(self, 'картошка')
#
#     def message(self):
#         print('potato')
#
#
# v = Vegetable('ovoproducto')
# p = Potato()
# v.message()
# p.message()
#
# - --- -- Алгоритмический тренажёр --  --- -
# #
# class Dog:
#     def __init__(self):
#         pass
#
# class Pudel(Dog):
#     def __init__(self):
#         Dog.__init__(self)
#
# class Beverage:
#     def __init__(self, bev_name):
#         self.__bev_name = bev_name
#
# class Cola(Beverage):
#     def __init__(self):
#         Beverage.__init__(self, 'coca-cola')
# -------------------------------- ЗАДАЧИ --------------------------------------------------------
#
# 1. Классы Employee и ProductionWorker
#
# import Employee
#
# def main():
#     name = input('Name: ')
#     emp_id = input('ID: ')
#     smena = int(input('Номер смены: '))
#     payrate = int(input('Ставка в час: '))
#
#     obj = Employee.ProductionWorker(name, emp_id, smena, payrate)
#
#     print('Name:', obj.get_name())
#     print('ID:', obj.get_emp_id())
#     print('Номер смены:', obj.get_smena())
#     print('Ставка в час:', obj.get_payrate())
#
#
# main()
# -----------------------------------------------------
#
# 2. Класс ShiftSupervisor
#
# import Employee
#
#
# def main():
#
#     name = input('Name: ')
#     emp_id = input('ID: ')
#     yearpay = int(input('Годовой оклад прораба: '))
#     bonus = int(input('Годовая премия прораба: '))
#
#     obj = Employee.ShiftSupervisor(name, emp_id, yearpay, bonus)
#
#     print('Имя: ', obj.get_name())
#     print('ID: ', obj.get_emp_id())
#     print('Годовой оклад: ', obj.get_year_pay())
#     print('Годовая премия: ', obj.get_bonus())
#     print(f'Общая З/П за год: {obj.get_year_pay() + obj.get_bonus()}')
#
#
# main()
# -------------------------------------------------------------------
#
# 3. класс Person and Customer
#
# class Person():
#     def __init__(self, name, adress, phone):
#         self.name = name
#         self.adress = adress
#         self.phone = phone
# 
#
# def set_flag(flag):
#     if flag == 1:
#         return True
#     elif flag == 0:
#         return False
#
#
# class Customer(Person):
#     def __init__(self, name, adress, phone, number, flag):
#         Person.__init__(self, name, adress, phone)
#         self.number = number
#         self.flag = flag
#
#
# def main():
#     name = input('Name: ')
#     adress = input('Adress: ')
#     phone = int(input('Phone: '))
#     number = int(input('Client number: '))
#     flag = int(input('Client in Newslatter? 1 - Yes, 0 - No: '))
#
#     obj = Customer(name, adress, phone, number, flag)
#
#     print('Name: ', obj.name)
#     print('Adress: ', obj.adress)
#     print('Phone: ', obj.phone)
#     print('Client number: ', obj.number)
#     x = obj.flag
#     if x:
#         print('Включить в рассылку.')
#     else:
#         print('Не включать в рассылку.')
#
#
# main()