
class student:

    college = "ABC"

    def display(self):
        print(self.college)

    @classmethod
    def show_college(cls):
        print(cls.college)

    @staticmethod
    def add(a,b):
        return a+b
    
student1 = student()
student1.display()
student.show_college()
print(student.add(6,7))