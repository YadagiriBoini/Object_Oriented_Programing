
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def deposite(self,amount):
        if amount>0:
            self.__balance += amount

    @property
    def balance(self):
        return self.__balance

account = BankAccount(5000)
print("Before Deposite:",account.balance)
account.deposite(200)                        # User don't nned to the logic behide the depositing money
print("After Deposite:",account.balance)