# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_hi(self):
#         return f'Person {self.name} says hello'
#
#     @staticmethod
#     def my_func():
#         return 'my func result'
#
# p = Person('Petar', 23)
# print(p.say_hi())
# print(Person.my_func())

# class Calculator:
#     def __init__(self, expression):
#         self.expression = expression
#
#     def calculate(self):
#         parts = self.parse_expression(self.expression)
#         print(parts)
#         return 0
#
#     @staticmethod
#     def parse_expression(expression):
#         parts = expression.split()
#         return parts
#
# c = Calculator('2 + 2 + 1 - 0')
# print(c.calculate())

# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#
#     @classmethod
#     def pepperoni(cls):
#         return cls(['tomato souse', 'parmesan', 'pepperoni'])
#
#     @classmethod
#     def margarita(cls, extra_ingredients=None):
#         ingredients = ['tomato sauce', 'mozarela']
#         if extra_ingredients:
#             ingredients.extend(extra_ingredients)
#         return cls(ingredients)
#
# p = Pizza.pepperoni()
# print(p.ingredients)
# margarita = Pizza.margarita(['adas', 'ghgh'])
# print(margarita.ingredients)
class Validator:
    @staticmethod
    def raise_if_str_is_null_or_empty(value):
        if not value.strip():
            raise ValueError('Invalid string')

    @staticmethod
    def raise_if_number_is_not_in_range(value, min_range, max_range, error_message):
        if value < min_range or value > max_range:
            raise ValueError(error_message)


class Person:
    MIN_AGE = 0
    MAX_AGE = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_str_is_null_or_empty(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.raise_if_number_is_not_in_range(
            value,
            self.MIN_AGE,
            self.MAX_AGE,
            f"Age should be between {self.MIN_AGE} and {self.MAX_AGE}"
        )
        self.__age = value


class Employee(Person):
    MIN_AGE = 16
    MAX_AGE = 160

    def __init__(self, name, age):
        super().__init__(name, age)


p = Person('Ivan', 13)
e = Employee('Gosho', 2)


