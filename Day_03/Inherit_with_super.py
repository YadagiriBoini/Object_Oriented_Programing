
class Animal:
    def sound(self):
        print("Animal makes sounds")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

dog = Dog()
dog.sound()