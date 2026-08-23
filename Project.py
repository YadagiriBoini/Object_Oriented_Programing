from abc import ABC, abstractmethod

class Person(ABC):                                       # Class Concept
    def __init__(self,name,age):                    # Constructor Concept
        self.name = name                            # Instance attribute Concept
        self.age = age

    @abstractmethod  
    def display_role(self):                         # Abstraction
        pass







class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_role(self):
        return "I am a teacher."







class Student(Person):                              # Inheritance Concept
    def __init__(self,name,age,course,marks):       # Inheritance + super() Concept
        super().__init__(name,age)
        self.course = course
        self.marks = marks

    def display_role(self):
        return "I am a Student."


    @property                                       # Encapsulation / Getter Concept
    def marks(self):                                # Getter method Concept
        return self.__marks                         # Private attribute access Concept

    @marks.setter                                   # Encapsulation / Setter Concept
    def marks(self,value):                          # Setter method Concept
        if 0 <= value <= 100:
            self.__marks = value
        else:
            raise ValueError("Invalid marks")       # Exception handling / validation Concept
        

    @property
    def age(self):
        return self._age                            # Protected-style attribute Concept

    @age.setter
    def age(self,value):
        if 0 <= value <= 25:
            self._age = value
        else:
            raise ValueError("Student age must be between 0 and 25")
        

    def display(self):                              # Instance method Concept
        return f"Name: {self.name} \nAge: {self.age} \nCourse: {self.course} \nMarks: {self.__marks}"

    def is_passed(self):                            # Instance method Concept
        if(self.__marks >= 40):
            return "Student is: Passed"
        return "Student is: Failed"

    def __str__(self):                              # Magic method Concept
        return f"{self.name} - {self.age} - {self.course} - {self.__marks} "






    

class StudentManager:
    def __init__(self):
        self.students = []                          # Object aggregation/composition Concept
 
    def add_student(self, student):
        self.students.append(student)               # Object aggregation/composition Concept

    def display_all(self):
        for i in self.students:                     # Object collection Concept
            print(i)

    def find_student(self, name):
        for i in self.students:                     # Object collection Concept
            if name == i.name:
                return i
        return "Student not found"
            
    def remove_student(self,name):
        for i in self.students:
            if name == i.name:
                self.students.remove(i)             # Object management Concept
                return "Student removed successfully",i.name,i.age, i.course, i.marks
        return "Student not found"






manager = StudentManager()                         # Object creation / Instantiation

# Students
std1 = Student("Yadagiri",20,"AIML",49)
std2 = Student("Ram",21,"IOT",78)   
std3 = Student("Sam",20,"AIDS",80)
std4 = Student("Joe",19,"CS",99)
std5 = Student("Root",22,"AIML",95)

# Teachers
teacher1 = Teacher("Miss Kavya", 25, "Python")
teacher2 = Teacher("Mr Anil", 37, "Java")
teacher3 = Teacher("Mrs Laxmi", 38, "C++")


# Add Students to StudentManager
manager.add_student(std1)
manager.add_student(std2)
manager.add_student(std3)
manager.add_student(std4)
manager.add_student(std5)


people = [                                        # Polymorphism
    std1,
    std2,
    std3,
    std4,
    std5,
    teacher1,
    teacher2,
    teacher3  
]


for person in people:
    print(person.display_role())

print()
print("All Student Info: ")
manager.display_all()
print(manager.find_student("Ram"))                 # Object interaction
print()
print(manager.remove_student("Joe"))
print()
print("Student After Removed one: ")
manager.display_all()