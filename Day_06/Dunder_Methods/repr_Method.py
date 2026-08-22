
class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):    #  Developer/debugging-friendly
        return f"Hi! I am {self.name} and I'm {self.age} year old."

emp1 = Employee("Varun",27)
print(repr(emp1))            