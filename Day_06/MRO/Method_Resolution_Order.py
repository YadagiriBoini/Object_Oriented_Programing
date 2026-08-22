
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")   # Self becomes B

class C(A):
    def show(self):
        print("C")   # Self becomes C

class D(B,C):        # Oder of (B ,C)
    pass


d = D()
d.show()   # First from the order => B
print(D.mro()) # D -> B -> C ->  A