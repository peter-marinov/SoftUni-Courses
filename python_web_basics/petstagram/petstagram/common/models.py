from django.db import models
from petstagram.photos.models import Photo


# Create your models here.
class Comment(models.Model):
    comment_text = models.TextField(
        max_length=300,
        blank=False,
        null=False,
    )
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.RESTRICT)

    # CASCADE: delete 1 photo and delete all connected comments
    # RESTRICT/PROTECT: delete 1 photo only if no connected comments
    # SET_NULL: delete 1 photo and set null for FK at comments

    class Meta:
        ordering = ['-date_time_of_publication']

class Like(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.RESTRICT)
