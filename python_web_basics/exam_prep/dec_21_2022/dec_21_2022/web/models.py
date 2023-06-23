from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
def check_if_first_letter_is_upper(value):
    if not value[0].isupper():
        raise ValidationError('Your name must start with a capital letter!')


def check_if_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Plant name should contain only letters!')


class Profile(models.Model):
    USERNAME_LEN_MAX = 10
    USERNAME_LEN_MIN = 2
    FIRST_NAME_LEN_MAX = 20
    LAST_NAME_LEN_MAX = 20

    username = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        validators=[
            validators.MinLengthValidator(USERNAME_LEN_MIN),
        ]
    )

    first_name = models.CharField(
        null=False,
        blank=False,
        verbose_name='First name',
        max_length=FIRST_NAME_LEN_MAX,
        validators=[
            check_if_first_letter_is_upper,
        ]
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=LAST_NAME_LEN_MAX,
        validators=[
            check_if_first_letter_is_upper,
        ]
    )

    profile_picture = models.URLField(
        null=True,
        blank=True
    )


class Plant(models.Model):
    PLANT_TYPE_LEN_MAX = 14
    NAME_LEN_MAX = 20
    NAME_LEN_MIN = 2

    OUTDOOR_PLANTS = 'Outdoor Plants'
    INDOOR_PLANTS = 'Indoor Plants'

    DIFFERENT_PLANTS = (
        (OUTDOOR_PLANTS, OUTDOOR_PLANTS),
        (INDOOR_PLANTS, INDOOR_PLANTS)
    )

    plant_type = models.CharField(
        null=False,
        blank=False,
        max_length=PLANT_TYPE_LEN_MAX,
        choices=DIFFERENT_PLANTS,
    )

    name = models.CharField(
        null=False,
        blank=False,
        max_length=NAME_LEN_MAX,
        validators=[
            validators.MinLengthValidator(NAME_LEN_MIN),
            check_if_only_letters,
        ]
    )

    image_url = models.URLField(
        null=False,
        blank=False
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False
    )