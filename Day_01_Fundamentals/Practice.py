
# Task - 1

class Car:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model =  model
        self.price = price

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price}")

car1 = Car("Audi","i200",10000000)
car1.display_info()


print()


# Task - 2

class Student:
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"My name is {self.name} I'm {self.age} years old studying in {self.course} branch")

student = Student("Yadagiri",20,"AIML")
student.introduce()


print()



# Task - 3

student1 = Student("Yadagiri",20,"AIML")
student2 = Student("Anil",22,"IOT")
student1.introduce()
student2.introduce()