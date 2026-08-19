
# Task - 1
class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(self.name,"is eating")

    def sleep(self):
        print(self.name,"is Sleeping")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed =breed

    def bark(self):
        print(self.name,"barks")

dog = Dog("Bruno","German Shepheard")
print(dog.name)
dog.eat()
dog.sleep()
print(dog.breed)
dog.bark()





# Task - 2
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"I'm {self.name}, I get {self.salary} salary.")
    
class Manager(Employee):
        def __init__(self, name, salary,department):
            super().__init__(name, salary)
            self.department = department

        def display(self):
             super().display()
             print(f"I'm {self.name}, I'm from {self.department} department. I get {self.salary} salary.")

manager = Manager("Sam",50000,"Testing")
manager.display()






# Task - 3
class Person:
    def eat(self):
        print("Person eats")

class Employee(Person):
    def work(self):
        print("Employee works")

class Manager(Employee):
    def manage(self):
        print("Manager manage the work")

manager = Manager()
manager.eat()
manager.work()
manager.manage()






# Task - 4
class Father:
    def driving(self):
        print("Drives car")

class Mother:
    def cooking(self):
        print("Cooks food")

class Child(Father, Mother):
    pass

child =Child()
child.driving()
child.cooking()    