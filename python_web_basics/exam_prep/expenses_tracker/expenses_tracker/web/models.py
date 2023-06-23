from django.core import validators
from django.db import models

from expenses_tracker.web.validators import validate_if_only_letters, MaxFileSizeValidator


# Create your models here.
class Profile(models.Model):
    FIRST_NAME_LEN_MAX = 15
    FIRST_NAME_LEN_MIN = 2

    LAST_NAME_LEN_MAX = 15
    LAST_NAME_LEN_MIN = 2

    BUDGET_DEFAULT_VALUE = 0
    BUDGET_MIN_VALUE = 0

    IMAGE_MAX_SIZE_IN_MB = 5
    UPLOAD_TO_DIR = 'profile/'

    first_name = models.CharField(
        # null=False,
        # blank=False,
        max_length=FIRST_NAME_LEN_MAX,
        validators=[
            validators.MinLengthValidator(FIRST_NAME_LEN_MIN),
            validate_if_only_letters,
        ],
        verbose_name='First name'
    )

    last_name = models.CharField(
        # null=False,
        # blank=False,
        max_length=LAST_NAME_LEN_MAX,
        validators=[
            validators.MinLengthValidator(LAST_NAME_LEN_MIN),
            validate_if_only_letters,
        ],
        verbose_name='Last name'
    )

    budget = models.FloatField(
        # null=False,
        # blank=False,
        default=BUDGET_DEFAULT_VALUE,
        validators=[
            validators.MinValueValidator(BUDGET_MIN_VALUE)
        ]
    )

    profile_image = models.ImageField(
        upload_to=UPLOAD_TO_DIR,
        null=True,
        blank=True,
        validators=(
            MaxFileSizeValidator(IMAGE_MAX_SIZE_IN_MB),
        )
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Expense(models.Model):
    TITLE_LEN_MAX = 30

    title = models.CharField(
        max_length=TITLE_LEN_MAX
    )

    expense_image = models.URLField(
        null=False,
        blank=False,
        verbose_name='Link to image'
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    price = models.FloatField()

    class Meta:
        ordering = ['pk']