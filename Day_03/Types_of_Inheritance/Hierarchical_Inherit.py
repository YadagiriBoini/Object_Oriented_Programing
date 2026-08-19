
class Animal:
    def __init__(self,name):
        self.name = name

    def sleep(self):
        print(self.name,"Sleeps")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print(self.name,"barks")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def meow(self):
        print(self.name,"Meows")

dog = Dog("Bruno")
cat = Cat("Kitty")

dog.sleep()
dog.bark()

cat.sleep()
cat.meow()