# use of functions in classes
# instance methods
# special methods

class Student:
    def __init__(self, name, id, age, college):
        self.name = name
        self.id = id
        self.age = age
        self.college = college

    # instance methods
    def stuf(self):  # with self
        print(f"The student age is {self.age}")

    def stufaddress(self, address):  # with parameter
        print(f"The student {self.name} lives in {address}")

    def info(self):  # with return
        info = f"name = {self.name},age = {self.age}, id = {self.id}, college = {self.college}"
        return info

    def __str__(self):  # automatically converts into strings
        info = f"name = {self.name},age = {self.age}, id = {self.id}, college = {self.college}"
        return info

    def __eq__(self, other):  # for comparison
        return self.name == other.name and self.age == other.age

    @staticmethod
    def salary_age(age):
        if age < 25:
            return 5000
        if age > 30:
            return 7000


s1 = Student("David", 230, 21, "MIT")
s1_dup = Student("David", 230, 21, "MIT")  # duplicate of s1 for comparison
s1.stuf()
s1.stufaddress("newyork")
print(s1.info())
print(s1)
print(s1 == s1_dup)
print(Student.salary_age(20))
print(s1.salary_age(31))
