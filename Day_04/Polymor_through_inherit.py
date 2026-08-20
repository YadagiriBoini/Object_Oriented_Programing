
class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print("Animal make sound")



class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print(self.name,"barks")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print(self.name,"meows")
        

# dog = Dog("Bruno")
# cat = Cat("Kitty")
# dog.sound()
# cat.sound()

animals = [Dog("Bruno"), Cat("Kitty")]
for animal in animals:
    animal.sound()