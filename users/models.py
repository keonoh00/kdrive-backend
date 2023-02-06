from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # overriding the parent class
    first_name = models.CharField(("first name"), max_length=150, editable=False)
    last_name = models.CharField(("last name"), max_length=150, editable=False)

    name = models.CharField(("name"), max_length=150, default="")

    pass
