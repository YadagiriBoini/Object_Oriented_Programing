
# Task - 1
class Empolyee:

    company = "HCL"

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"I'm  {self.name}, I work in {self.company}, I earn about {self.salary} a month.")

    @classmethod
    def company_info(cls):
        print("Company name is",cls.company)

    @staticmethod
    def is_valid_salary(salary):
        return salary>15000

empolyee1 = Empolyee("Yadagiri", 50000)
empolyee2 = Empolyee("Anil", 60000)
empolyee1.display()
Empolyee.company_info()
print(Empolyee.is_valid_salary(50000))





# Task - 2
class student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls,data):
        name,age = data.split(",")
        return cls(name, int(age))

student1 = student.from_string("Yadagiri,20")
print(student1.name)
print(student1.age)





# Task - 3
    