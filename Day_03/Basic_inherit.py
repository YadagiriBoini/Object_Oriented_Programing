
class Animal:                         # Parent Class
    def eat(self):
        print("Animal is eating")

class Dog(Animal):                     # Child Class
    pass

dog = Dog()
dog.eat()