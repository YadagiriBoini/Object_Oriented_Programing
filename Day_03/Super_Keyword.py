
class Animal:

    def __init__(self,name):
        self.name = name

    def eat(self):
        print(self.name,"is eating")

class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed


dog = Dog("Bruno","German Shepherd")
print(dog.name)
print(dog.breed)