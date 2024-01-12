# Inheritance, Extend, Override
class Employee:  # parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print(f"{self.name} is working in this company and has age {self.age}")


class Dev(Employee):  # child class
    def __init__(self, name, age, salary):  # extend child class
        super().__init__(name, age)  # call parent class
        self.salary = salary

    def work(self):  # overriding
        print(f"{self.name} is developing")


class QA(Employee):
    def work(self):
        print(f"{self.name} is testing")


e1 = Employee("Tom", 25)
d1 = Dev("Andy", 30, 2000)
q1 = QA("Tom", 30)
# print(e1.name, e1.age)
# print(d1.name, d1.age)
# e1.work()
# d1.work()
# print(d1.salary)
# q1.work()

# Polymorphism
employees = [Dev("James", 32, 5000), QA("Ken", 25)]


def f_employees(employees):
    for e in employees:
        e.work()


f_employees(employees)
