
class A:

    def add(self,a,b):
        return a+b             # + acts as addition operator

    def concat(self,x,y):
        return x+y             # + acts as concatination operator

a1 = A()
print(a1.add(2,3))
print(a1.concat("Boini ","Yadagiri"))