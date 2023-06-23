from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class CheckIfYearInBetween:
    def __init__(self, min_year, max_year):
        self.min_year = min_year
        self.max_year = max_year

    def __call__(self, value):
        if self.min_year > value > self.max_year:
            raise ValidationError('The username must be a minimum of 2 chars')

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.min_year == other.min_year
            and self.max_year == other.max_year
        )
