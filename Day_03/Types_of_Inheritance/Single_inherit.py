
class Animal:
    def sound(self):
        print("Animal makes sounds")

class Dog(Animal):
    def barks(self):
        print("Dog barks")

dog = Dog()
dog.sound()
dog.barks()