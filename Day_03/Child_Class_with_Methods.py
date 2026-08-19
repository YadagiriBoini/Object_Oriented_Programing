
class Animal:                         # Parent Class
    def eat(self):
        print("Animal is eating")

class Dog(Animal):                     # Child Class
    def bark(self):
        print("Dog is barking")

dog = Dog()
dog.eat()
dog.bark()