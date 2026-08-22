
class Doctor:
    def treat(self, patient):
        print("Treating",patient.name)


class Patient:
    def __init__(self,name):
        self.name = name



p1 = Patient("Sankit")
d1 = Doctor()

d1.treat(p1)