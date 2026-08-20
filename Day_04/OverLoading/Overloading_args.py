
class Calculator:

    def add(self,*args):       # can implement method overloading using *args
        total = 0

        for num in args:
            total+=num

        return total
    
calcu = Calculator()
print(calcu.add(2,3))
print(calcu.add(4,6,8))
print(calcu.add(5,6,4,3,))
print(calcu.add(3,6,7,9,5))