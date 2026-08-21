
class BankAccount:

    def __init__(self,balance):
        self.__balance = balance   
 
account = BankAccount(10000)
print(account.__balance)           # Name Mangling    account._BankAccount__balance
