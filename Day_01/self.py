
class student:

    def study(self):                       # self refers to the current instance of the class
        print("Student is Studying")

student1 = student()
print(student1.study())


# self is not a python keyword it is a naming convetion
# We can also write:
"""class student:
    def study(this):
        print("Student is studying")"""
