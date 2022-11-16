class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        if self.students:
            average = sum(self.grades) / len(self.grades)
        else:
            average = 0
        return average

    def __repr__(self):
        return_sting = f"The students in {self.name}: {', '.join(self.students)}." \
                       f" Average grade: {Class.get_average_grade(self):.2f}"
        return return_sting







a_class = Class("11B")
# a_class.add_student("Peter", 4.80)
# a_class.add_student("George", 6.00)
# a_class.add_student("Amy", 3.50)

print(a_class)