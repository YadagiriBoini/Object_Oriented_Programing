"""

class Student:

    def __init__(self,name):
        self.name = name

s1 = Student("Yadagiri")
s2 = Student("Yadagiri")
print( s1 == s2 )          # Python doesn't consider them equal simply because their attributes are equal.


"""




class Student:

    def __init__(self,name):
        self.name = name

    def __eq__(self, value):
        return self.name == value.name

s1 = Student("Yadagiri")
s2 = Student("Yadagiri")
print(s1 == s2)            # True
