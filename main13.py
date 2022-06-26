# object oriented programming

class Employee:
    _name = None
    _id = 0
    _salary = 0

    def init_(self, name, id, salary):
        self._name = name
        self._id = id
        self._salary = salary


    def _set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def set_salary(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary

Sharika = Employee('Sharika', 420, 7000000)
print(Sharika.get_name())
