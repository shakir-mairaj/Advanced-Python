# class
# instance
# class attribute
# instance attribute

class Employee:
    # class attribute
    alias = "Engineer"

    def __init__(self, name, age, salary, role):
        # instance attributes
        self.name = name
        self.age = age
        self.salary = salary
        self.role = role


# instance
e1 = Employee("james", 28, 5000, "Dev")
print(e1.name, e1.age, e1.salary, e1.role)  # only for one instance
print(Employee.alias)  # same for every instance
print(e1.alias)