# Encapsulation

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None  # internal private attribute #protected #you can access it from outside but you shouldn't
        self._bugs_resolved = 0
        self.__id = None  # completely private, can't be accessed from outside

    def code(self):
        self._bugs_resolved += 1

    # getter
    def get_salary(self):
        return self._salary

    # setter
    # can be used to check value,enforce conditions
    def set_salary(self, value):
        self._salary = self._calculate_salary(value)

    def _calculate_salary(self, value):
        if self._bugs_resolved < 10:
            return value
        if self._bugs_resolved < 100:
            return value * 2
        return value * 3


e1 = Employee("Kane", 30)
e1.set_salary(5000)
print(e1.get_salary())

for i in range(70):  # no of bugs solved
    e1.code()
e1.set_salary(5000)
print(e1.get_salary())
