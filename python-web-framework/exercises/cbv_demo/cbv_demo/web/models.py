from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


def check_if_only_letters(value):
    if not value.isalpha():
        raise ValidationError('The title must be only letters')


# Create your models here.
class Article(models.Model):
    title = models.CharField(
        max_length=30,
        validators=[
            check_if_only_letters,
        ]
    )

    info = models.TextField(
        null=False,
        blank=False,
        max_length=20,
    )

    def get_absolute_url(self):
        return reverse('detail_view', kwargs={'pk': self.pk})