
class Employee:
    def __init__(self):
        self._salary = 50000     # Protetced

    def info(self):
        return "My slary is",self._salary


emp1 = Employee()
print(emp1._salary)
print(emp1.info())