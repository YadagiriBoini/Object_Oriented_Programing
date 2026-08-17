
class Student:

    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

    def intro(self):
        print(f"My name is {self.name} and I'm {self.age} years old. Studying in {self.course}")

Student1 = Student("Yadagiri",20,"CSE")
Student1.intro()