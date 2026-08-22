

# A Department has a Teacher.

class Teacher:                      # A teacher can exist even if the department is removed.
    def __init__(self,name):
        self.name = name


class Department:
    def __init__(self, teacher):
        self.teacher = teacher


t1 = Teacher("Sam")       # Teacher is independent 
d1 = Department(t1)
print(d1.teacher.name)


# Composition → Strong HAS-A
# Aggregation  → Weak HAS-A
