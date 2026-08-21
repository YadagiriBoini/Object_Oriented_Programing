
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def set_balance(self,amount):
        if amount>0:
            self.__balance += amount


    @property
    def balance(self):
        return self.__balance

account1 = BankAccount(5000)
print("Before  Deposite",account1.balance)   
account1.set_balance(500)
print("After Deposite:",account1.balance)   