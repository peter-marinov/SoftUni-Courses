class StudentTaxes:
    def __init__(self, name, semester_tax, average_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.average_grade = average_grade

    def get_discount(self):
        # Violation if there was case when you have None from missing return
        if self.average_grade > 5:
            return self.semester_tax * 0.4
        return 0


class AdditionalDiscount(StudentTaxes):
    def get_discount(self):
        result = super().get_discount()
        if result:
            return result
        if 4 < self.average_grade <= 5:
            return self.semester_tax * 0.2
        return 0

st = [
    StudentTaxes('Doncho', 1000, 4.5),
    StudentTaxes('Pesho', 1000, 5.5),
    AdditionalDiscount('Maria', 1000, 4.6),
    AdditionalDiscount('Stamat', 1000, 5.6),
]
[print(s.get_discount()) for s in st]