
class student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):               # instance method
        print(f"I am {self.name} I'm {self.age} years old.")

student1 = student("Yadagiri",20)
student1.intro()
