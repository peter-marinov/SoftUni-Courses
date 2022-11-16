from inheritance_exercise.person import Employee
from inheritance_exercise.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'