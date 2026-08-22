"""


class Student:
    def __init__(self,name,age):
        self.name =  name
        self.age = age

student = Student("Yadagiri",20)
print(student)                    # <__main__.Student object at 0x00000216AB15B048> 


"""




class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hi! I am {self.name} and I'm {self.age} year old."

emp1 = Employee("Varun",27)
print(emp1)                     # Hi! I am Varun and I'm 27 year old.