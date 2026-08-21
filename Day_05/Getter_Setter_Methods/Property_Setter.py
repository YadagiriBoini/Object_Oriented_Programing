
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,amount):
        if amount>0:
            self.__balance += amount
        else:
            print("Invalid Balance")

acc1 = BankAccount(5000)
print("Before Deposite:",acc1.balance)
acc1.balance = 200
print("After Deposite:",acc1.balance)