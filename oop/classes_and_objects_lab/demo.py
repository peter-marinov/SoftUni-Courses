'''
class Fraction:
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator

    def __add__(self, other):
        nominator = self.nominator * other.denominator + \
            other.nominator * self.denominator
        denominator = self.denominator * other.denominator

        return Fraction(nominator, denominator)

    def __str__(self):
        return f'{self.nominator}/{self.denominator}'

f1_2 = Fraction(1, 2)
print(f'{f1_2.nominator}/{f1_2.denominator}')
print(f1_2)
print(Fraction(1, 2) + Fraction(3, 4) + Fraction(2, 2))
'''

######

# ss = 'Doncho'
# print(str(ss))
# print(repr(ss))

'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}; Age: {self.age}'

    def __repr__(self):
        return f'Person("{self.name}", {self.age})'

p = Person('Doncho', 19)
print(str(p))
print(repr(p))
print(eval(repr(p)))
'''


class Person:
    min_age = 0
    max_age = 150

    def __init__(self, name, age):
        self.name = name    # instance properties / attributes
        self.age = age      # instance properties / attributes

    def __str__(self):
        return f'Name: {self.name}; Age: {self.age} ' \
            f'Min age: {self.min_age}; Max age: {self.max_age}'

print(Person('Doncho', 19))
Person.max_age = 160
print(Person('Maria', 23))
