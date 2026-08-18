
# Alternative of constructors

class student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name,age = data.split(",")
        return cls(name, int(age))

Student = student.from_string("Yadagiri,20")
print(Student.name)
print(Student.age)