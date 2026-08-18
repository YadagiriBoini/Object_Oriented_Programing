
# Class variable = Defined at class level and can be shared among all the instaces of a class

class student:

    college = "SVIT"

    def __init__(self,name,age,marks):
        self.name = name
        self.age = age                        

student1 = student("Yadagiri",20,89)
student2 = student("Ram",22,87)

print(f"My name is {student1.name} I'm {student1.age} years old I study in {student.college}")  #college can be accessed
print(f"My name is {student2.name} I'm {student2.age} years old I study in {student.college}")  #college can be accessed

# we we are refering to an class variable best to use 
# "Class_name.variable_name" instead of "iinstace_name.variable_name"