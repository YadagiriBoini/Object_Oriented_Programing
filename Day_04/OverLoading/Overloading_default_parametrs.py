
class Calculator:

    def add(self,a,b,c=0):    # can somewhat implement the overloaing 
        return a+b+c  

calcu = Calculator()
print(calcu.add(2,4))
print(calcu.add(3,5,7))