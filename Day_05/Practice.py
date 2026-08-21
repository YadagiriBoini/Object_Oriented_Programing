
# Task - 1
class BankAccount:

    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,amount):
        if amount>0:
            self.__balance += amount
        else:
            return "Invalid amount"

    def withdraw(self,amount):
        if self.__balance > amount:
            self.__balance -= amount
        else:
            return "Insufficient Balance"

    def get_balance(self):
        return self.__balance

acc1 = BankAccount(5000)
print("Before Deposit:",acc1.get_balance())
acc1.deposit(3000)
print("After Deposit:",acc1.get_balance())
acc1.withdraw(1500)
print("After Withdrawal:",acc1.get_balance())



print()
print()



# Taks - 2
class BankAccount:

    def __init__(self,balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,amount):
        if amount>=0:
            self.__balance = amount
        else:
            raise ValueError("Balance cannot be negative")    # "print("Invalid amount)"
    
        
acc1 = BankAccount(5000)
print("Before Setter:",acc1.balance)
acc1.balance = 3000
print("After Setter:",acc1.balance)




print()
print()




# Task - 3
from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Circle Area")

class Rectangle(Shape):
    def area(self):
        print("Rectangle Area")

# shape = Shape()    Error Because Shape has abstract methods
c1 = Circle()
r1 = Rectangle()
c1.area()
r1.area()
