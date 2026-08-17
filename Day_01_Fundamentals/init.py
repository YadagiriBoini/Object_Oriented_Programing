
# insted of writing 
""""
student1 = student()
student1.set_name("Yadagiri")
"""

# we can write in short
class student:

    def __init__(self,name,age,marks):     # we get an object containing name,age,marks attributes
        self.name = name
        self.age = age
        self.marks = marks

student1 = student("Yadagiri",20,78)

print(student1.name)
print(student1.age)
print(student1.marks)

# same Class  
# Different Objects 
# Different data