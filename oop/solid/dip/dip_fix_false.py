import abc


class Validator(abc.ABC):
    @abc.abstractmethod
    def validate(self, value):
        pass


class NumbersValidator(Validator):
    min_value = 0
    max_value = 1024

    def validate(self, value):
        if value < self.min_value or self.max_value < value:
            raise ValueError(f'Value is outside of the range [{self.min_value}, {self.min_value}]')


class NegativeNumbersValidator(NumbersValidator):
    min_value = -1024
    max_value = 0


class NumbersController:
    ValidatorClass = NumbersValidator()

    def __init__(self):
        self.numbers = []
        self.validator = self.ValidatorClass # This is violation to DIP

    def add_number(self, number):
        try:
            self.validator.validate(number)
            self.numbers.append(number)
        except:
            pass

    def __str__(self):
        return ', '.join(str(x) for x in self.numbers)


# This leads to subclass overloading
class NegativeNumbersController(NumbersController):
    ValidatorClass = NegativeNumbersValidator()

nc = NumbersController()
nc.add_number(1)
nc.add_number(2)
print(nc)
nc.add_number(-3)
print(nc)


nc = NegativeNumbersController()
nc.add_number(1)
nc.add_number(2)
print(nc)
nc.add_number(-3)
print(nc)