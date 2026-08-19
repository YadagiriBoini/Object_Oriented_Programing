
class Father:
    def skin_Tone(self):
        print("Dusky")

class Mother:
    def voice(self):
        print("Low pitch")

class Child(Father, Mother):
    def drink(self):
        print("Drinks milk")

child = Child()
child.skin_Tone()
child.voice()
child.drink()