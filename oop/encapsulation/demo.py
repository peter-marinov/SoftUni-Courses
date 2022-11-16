class Student:
    def __init__(self, number, id_number):
        self.number = number
        self.__id_number = id_number
        self._grades = [5, 6]

    def calculate_age(self):
        year = self.__id_number[:2]

    def get_id_number(self):
        return self.__id_number[:6] + '****'

    def set_id_number(self, val):
        if val[:2] != '90':
            raise ValueError('Only 90 students are accepted')
        self.__id_number = val


class UniversityStudent(Student):
    def clc_avg_grads(self):
        self._grades = 0


student = Student('1234a', "2001010101")
student.set_id_number('909090')
