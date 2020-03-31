# corey_Schafer-OOP/employee

# Employee_count = 0
# raise_amount = .04

class Employee():  #Create the class
    def __init__(self, first, last, pay): # init is the first method(?), it is named after the class
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # Employee_count += 1

    def fullname(self):
        return f'{self.last}, {self.first}'

    # def apply_raise(self):
    #     self.pay = int(self.pay * (1 + self.raise_amount))

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('CJ', 'Ricciardi', 60000)

# print(raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
print(emp_2.pay)