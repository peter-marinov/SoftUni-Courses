from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

# Create your models here

class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Book(models.Model):
    # Correct
    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING
    )
    # incorrect
   # profile = models.ForeignKey(Profile)