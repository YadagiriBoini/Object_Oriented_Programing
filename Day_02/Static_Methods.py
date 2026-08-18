
class Student:

    @staticmethod
    def is_adult(age):            # Independent logic doen't need self or cls
        return age>=18
    
print(Student.is_adult(20))