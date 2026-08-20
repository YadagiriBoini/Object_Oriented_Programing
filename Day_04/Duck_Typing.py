
class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

def make_sound(animal):     # make_sound() doesn't care about object it only cares about sound() like Dog()/Cat()
    animal.sound()

make_sound(Dog())
make_sound(Cat())   