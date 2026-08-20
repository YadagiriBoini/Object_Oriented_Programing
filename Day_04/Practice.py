
# Task - 1
class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print("Animal makes sound")


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


class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print(self.name,"moos")


animals = [Dog("Bruno"), Cat("Kitty"), Cow("Ponta")]

for animal in animals:
    animal.sound()



print()
print()



# Task - 2
class Dog:
    def speak(self):
        print("Barks")

class Cat:
    def speak(self):
        print("Meows")

class Human:
    def speak(self):
        print("hyy!")

def make_sound(x):
    x.speak()

make_sound(Dog())
make_sound(Cat())
make_sound(Human())



print()
print()



# Task - 3
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Point( self.x + other.x,
                      self.y + other.y )

p1 = Point(10,80)
p2 = Point(50,40)

p3 = p1+p2

print(p3.x)
print(p3.y)