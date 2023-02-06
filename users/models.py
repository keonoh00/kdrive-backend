from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    # overriding the parent class
    first_name = models.CharField(("first name"), max_length=150, editable=False)
    last_name = models.CharField(("last name"), max_length=150, editable=False)

    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KOREAN = ("kr", "Korean")
        ENGLISH = ("en", "English")

    name = models.CharField(("name"), max_length=150, default="")

    avatar = models.ImageField(blank=True)
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    language = models.CharField(
        max_length=10,
        choices=LanguageChoices.choices,
    )

    def __str__(self) -> str:
        return self.name
