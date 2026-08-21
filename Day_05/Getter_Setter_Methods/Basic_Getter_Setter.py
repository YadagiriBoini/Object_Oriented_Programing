
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def set_balance(self,amount):          
        if amount > 0:
            self.__balance += amount    # Setter

    def get_balance(self):
        return self.__balance           # Getter

account1 = BankAccount(5000)
print("Before Deposite:",account1.get_balance())
account1.set_balance(500)
print("After Deposite:",account1.get_balance())