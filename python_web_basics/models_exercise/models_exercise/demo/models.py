import datetime

from django.db import models


# Create your models here.
class ZodiacMixin(models.Model):
    zodiac = models.CharField(max_length=10)

    class Meta:
        abstract=True


class Cities(models.Model):
    city_name = models.CharField(
        max_length=10,
        unique=True
    )

    def __str__(self):
        return self.city_name


class People(ZodiacMixin, models.Model):
    class Meta:
        ordering = ['-age']

    LEVEL_BABY = 'Baby'
    LEVEL_TEEN = 'Teen'
    LEVEL_OLD = 'Old'

    LEVELS = (
        (LEVEL_BABY, LEVEL_BABY),
        (LEVEL_TEEN, LEVEL_TEEN),
        (LEVEL_OLD, LEVEL_OLD),
    )

    first_name = models.CharField(
        max_length=30,
        unique=True
    )
    level = models.CharField(
        max_length=10,
        choices=LEVELS,
        # default='Old'
    )
    age = models.IntegerField()
    city = models.CharField(max_length=10)
    city_id = models.ForeignKey(
        'Cities',
        on_delete=models.RESTRICT
    )
    created_on = models.DateTimeField(auto_now_add=True)

    @property
    def born_in(self):
        return datetime.date.today().year - self.age

    def __str__(self):
        return f'User {self.first_name} is {self.level}. He/She is {self.age} old and from {self.city}'


