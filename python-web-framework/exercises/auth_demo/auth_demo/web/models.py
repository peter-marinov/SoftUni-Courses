from django.db import models
from django.contrib.auth import models as auth_models
# Create your models here.


class Person(auth_models.User):
    pass
