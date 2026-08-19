

class Animal:
    def sound(self):
        print("Animal makes Sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def woofie(self):
        print("Puppy woofies")

puppy = Puppy()
puppy.woofie()