from django.db import models


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    image_url = models.URLField(verbose_name='Link to Profile Image')


class Note(models.Model):
    title = models.CharField(max_length=30)
    context = models.TextField()
    image_url = models.URLField(verbose_name='Link to Image')

    class Meta:
        ordering = ['id']
