class Patient:
    def __init__(self, fio, adress, phone, sos):
        self.__fio = fio
        self.__adress = adress
        self.__phone = phone
        self.__sos = sos

    def set_fio(self, fio):
        self.__fio = fio

    def set_adress(self, adress):
        self.__adress = adress

    def set_phone(self, phone):
        self.__phone = phone

    def set_sos(self, sos):
        self.__sos = sos

    def get_fio(self):
        return self.__fio

    def get_adress(self):
        return self.__adress

    def get_phone(self):
        return self.__phone

    def get_sos(self):
        return self.__sos


class Procedure:
    def __init__(self, name, date, medic, price):
        self.__name = name
        self.__date = date
        self.__medic = medic
        self.__price = price

    def set_name(self, name):
        self.__name = name

    def set_date(self, date):
        self.__date = date

    def set_medic(self, medic):
        self.__medic = medic

    def set_price(self, price):
        self.__price = price

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_medic(self):
        return self.__medic

    def get_price(self):
        return self.__price