
class Animal:

    def __init__(self,name):
        self.name = name

    def eat(self):
        print(self.name,"is eating")

class Dog(Animal):
    pass

dog = Dog("Bruno")
print(dog.name)
dog.eat()

    