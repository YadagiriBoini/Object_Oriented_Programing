
class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print(self.name,"barks")      # Overriding the sound()

dog = Dog("Bruno")
dog.sound()