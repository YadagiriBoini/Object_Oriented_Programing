
# Task - 1
class Student:
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

    def __str__(self):
        return f"{self.name} - {self.course}"

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age}, course='{self.course}')"

s1 = Student("Yadagiri",20,"AIML")
print(s1)
print(repr(s1))




print()
print()





# Task - 2
class Team:
    def __init__(self,players):
        self.players = players

    def __len__(self):
        return len(self.players)

    def __eq__(self, other):
        return self.players == other.players

t1 = Team(["A", "B", "C", "D", "E"])
t2 = Team(["A", "B", "C", "D",])
print(len(t1))
print(len(t2))
print( t1 == t2 )




print()
print()



# Task - 3
# Composition
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car Started")
c1 = Car()
c1.start()



print()
print()



# Taks - 4
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def  show(self):
        print("C")

class D(B,C):
    pass

d = D()
d.show()  # B
print(D.mro())  # D -> B -> C -> A -> Object