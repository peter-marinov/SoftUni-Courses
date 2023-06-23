from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models

from oct_30_2022.web.validators import CheckIfYearInBetween


def check_if_year_in_between(value):
    print([value])
    if Car.YEAR_MIN > value or Car.YEAR_MAX < value:
        raise ValidationError('Year must be between 1980 and 2049')


# Create your models here.
class Profile(models.Model):
    USERNAME_LEN_MAX = 10
    USERNAME_LEN_MIN = 2
    AGE_VALUE_MIN = 18
    PASSWORD_LEN_MAX = 30
    FIRST_NAME_LEN_MAX = 30
    LAST_NAME_LEN_MAX = 30

    username = models.CharField(
        null=False,
        blank=False,
        max_length=USERNAME_LEN_MAX,
        # TODO: check if the error msg is correct when is less than 2
        validators=[
            validators.MinLengthValidator(
                USERNAME_LEN_MIN,
                'The username must be a minimum of 2 chars'
            ),
        ]
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            validators.MinValueValidator(AGE_VALUE_MIN)
        ]
    )

    password = models.CharField(
        max_length=PASSWORD_LEN_MAX,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=FIRST_NAME_LEN_MAX
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=LAST_NAME_LEN_MAX
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Car(models.Model):
    MODEL_LEN_MAX = 20
    MODEL_LEN_MIN = 2
    YEAR_MIN = 1980
    YEAR_MAX = 2049
    PRICE_MIN = 1

    SPORTS_CAR = 'Sports Car'
    PICKUP = 'Pickup'
    CROSSOVER = 'Crossover'
    MINIBUS = 'Minibus'
    OTHER = 'Other'
    CAR_TYPES = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )

    type = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        choices=CAR_TYPES,
    )

    model = models.CharField(
        null=False,
        blank=False,
        max_length=MODEL_LEN_MAX,
        validators=[
            validators.MinLengthValidator(MODEL_LEN_MIN)
        ],
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            check_if_year_in_between,
        ]
    )

    image_url = models.URLField(
        null=False,
        blank=False
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[
            validators.MinValueValidator(PRICE_MIN)
        ]
    )