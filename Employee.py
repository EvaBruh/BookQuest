class Employee:
    def __init__(self, name, emp_id):
        self.__name = name
        self.__emp_id = emp_id

    def set_name(self, name):
        self.__name = name

    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    def get_name(self):
        return self.__name

    def get_emp_id(self):
        return self.__emp_id


class ProductionWorker(Employee):
    def __init__(self, name, emp_id, smena, payrate):
        Employee.__init__(self, name, emp_id)
        self.__smena = smena
        self.__payrate = payrate

    def set_smena(self, smena):
        self.__smena = smena

    def set_payrate(self, payrate):
        self.__payrate = payrate

    def get_smena(self):
        return self.__smena

    def get_payrate(self):
        return self.__payrate


class ShiftSupervisor(Employee):
    def __init__(self, name, emp_id, year_pay, bonus):
        Employee.__init__(self, name, emp_id)
        self.__year_pay = year_pay
        self.__bonus = bonus

    def set_year_pay(self, year_pay):
        self.__year_pay = year_pay

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_year_pay(self):
        return self.__year_pay

    def get_bonus(self):
        return self.__bonus
