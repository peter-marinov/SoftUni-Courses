from django.core import validators
from django.db import models


# Create your models here.
class ProfileModel(models.Model):
    email = models.EmailField(
        null=False,
        blank=False
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            validators.MinValueValidator(12)
        ]
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True
    )


class GameModel(models.Model):
    choices_list = ["Action", "Adventure", "Puzzle", "Strategy", "Sports", "Board/Card Game", "Other"]
    CATEGORIES = [(category, category) for category in choices_list]

    title = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        unique=True
    )

    category = models.CharField(
        max_length=15,
        choices=CATEGORIES
    )

    rating = models.FloatField(
        null=False,
        blank=False,
        validators=[
            validators.MinValueValidator(0.1),
            validators.MaxValueValidator(5.0),
        ]
    )

    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            validators.MinValueValidator(1),
        ]
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )


