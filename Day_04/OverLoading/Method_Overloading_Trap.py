
class Calculator:
    def add(self,a,b):
        return a+b

    def add(self,a,b,c):    # Override the first funtion
        return a+b+c
print(Calculator().add(2,3,6))

