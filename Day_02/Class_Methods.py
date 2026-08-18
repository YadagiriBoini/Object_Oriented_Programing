
class student:

    college = "SVIT"

    @classmethod
    def show_college(cls):                         # current class
        print(f"College name is {cls.college}")

student.show_college()


# self → current object
# cls  → current class