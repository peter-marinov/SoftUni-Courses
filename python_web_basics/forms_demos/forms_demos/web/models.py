from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
def validate_name(value):
    first_and_last_name = value.split(' ')
    if len(first_and_last_name) != 2:
        raise ValidationError('Must include first and last anmes')


class Pet(models.Model):
    MAX_NAME_LENGTH = 30
    name = models.CharField(
        max_length=MAX_NAME_LENGTH
    )

    def __str__(self):
        return self.name


class Person(models.Model):
    MAX_LANE_LENGTH = 35
    name = models.CharField(
        max_length=MAX_LANE_LENGTH,
        validators=(validate_name, )
    )

    age = models.PositiveIntegerField()

    pets = models.ManyToManyField(
        Pet,
    )