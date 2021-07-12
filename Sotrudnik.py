class Employee:
    def __init__(self, fisrt, last, pay):
        self.first = fisrt
        self.last = last
        self.pay = pay

    def give_raise(self, pay=''):
        if pay:
            self.pay = pay
        else:
            self.pay += '5000'
        return f'{self.pay}'