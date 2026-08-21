
class BankAccount:

    def __init__(self,balance):
        self.__balance = balance    # Private
 
    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance
    

account = BankAccount(5000)
account.deposite(500)
print(account.get_balance())

# we use access_convention so that no can do:
# account.balance = -5000