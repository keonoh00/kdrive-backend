from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    # overriding the parent class and disabling the field
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)

    name = models.CharField(max_length=150, default="")

    avatar = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.name
