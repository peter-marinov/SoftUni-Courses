from django.core import validators
from django.db import models

from fruitipedia.web.validators import check_if_string_starts_with_letter, check_if_string_only_letters


# Create your models here.
class ProfileModel(models.Model):
    FIRST_NAME_LEN_MAX = 25
    FIRST_NAME_LEN_MIN = 2

    LAST_NAME_LEN_MAX = 35
    LAST_NAME_LEN_MIN = 1

    EMAIL_LEN_MAX = 40

    PASSWORD_LEN_MAX = 20
    PASSWORD_LEN_MIN = 8

    AGE_DEFAULT_VALUE = 18

    first_name = models.CharField(
        max_length=FIRST_NAME_LEN_MAX,
        validators=[
            validators.MinLengthValidator(FIRST_NAME_LEN_MIN),
            check_if_string_starts_with_letter,
        ],
        verbose_name='First Name'
    )

    last_name = models.CharField(
        max_length=LAST_NAME_LEN_MAX,
        validators=[
            validators.MinLengthValidator(LAST_NAME_LEN_MIN),
            check_if_string_starts_with_letter,
        ],
        verbose_name='Last Name'
    )

    email = models.EmailField(
        max_length=EMAIL_LEN_MAX
    )

    password = models.CharField(
        max_length=PASSWORD_LEN_MAX,
        validators=[
            validators.MinLengthValidator(PASSWORD_LEN_MIN)
        ]
    )

    image_url = models.URLField(
        verbose_name='Image URL',
        null=True,
        blank=True,
    )

    age = models.IntegerField(
        default=AGE_DEFAULT_VALUE,
        null=True,
        blank=True
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class FruitModel(models.Model):
    NAME_LEN_MAX = 30
    NAME_LEN_MIN = 2

    name = models.CharField(
        max_length=NAME_LEN_MAX,
        validators=[
            validators.MinLengthValidator(NAME_LEN_MIN),
            check_if_string_only_letters,
        ]
    )

    image_url = models.URLField(
        verbose_name='Image URL'
    )

    description = models.TextField()

    nutrition = models.TextField(
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['pk']

