# Class banes are always PascalCase
class Person:
    def __init__(self, name, age):
        # constructor
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} - year old'

    def increased_age(self):
        self.age += 1

p1 = Person('Ivan', 30)
p2 = Person('Ivan', 30)
print(p1)
p1.increased_age()
print(p1)