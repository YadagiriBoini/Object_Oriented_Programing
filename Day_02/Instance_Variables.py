
# Instance variable = value is specific to an individual object

class student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age                        # name,age,marks are the intace variables
        self.marks = marks

student1 = student("Yadagiri",20,89)
student2 = student("Ram",22,87)

print(f"My name is {student1.name} I'm {student1.age} years old I have obtained {student1.marks} marks")
print(f"My name is {student2.name} I'm {student2.age} years old I have obtained {student2.marks} marks")
print()

# if a change happend 
student1.age = 21                     # change happens onlt in student1 not in other objects

print()
print(f"My name is {student1.name} I'm {student1.age} years old I have obtained {student1.marks} marks")
print(f"My name is {student2.name} I'm {student2.age} years old I have obtained {student2.marks} marks")