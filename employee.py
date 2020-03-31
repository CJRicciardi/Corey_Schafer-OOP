# corey_Schafer-OOP/employee

class Employee():  #Create the class

    num_of_emps = 0
    raise_amt = .04

    def __init__(self, first, last, pay): # init is the first method(?), it is named after the class
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.last}, {self.first}'

    def apply_raise(self):
        self.pay = int(self.pay * (1 + self.raise_amount))

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

import datetime
my_date = datetime.date(2016, 8, 10)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('CJ', 'Ricciardi', 60000)

print(Employee.is_weekday(my_date))