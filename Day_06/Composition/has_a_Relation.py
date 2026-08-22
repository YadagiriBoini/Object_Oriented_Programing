

# A Car has a Engine.

class Engine:
    def start(self):
        print("Engine Started")



class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car Started")


c1 = Car()
c1.start()

# IS-A  → Inheritance
# HAS-A → Composition
