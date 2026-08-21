 
from abc import ABC, abstractmethod     # ABC = Abstarct Base Class

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Barks")



# animal = Animal()     Animal has an abstract method that hasn't been implemented
dog = Dog()
dog.sound()