from django.db import models
from common.models import CommonModel
from .image_classes import CIFAR100ImageClasses


class Image(CommonModel):

    """Image Model Definition"""

    file_name = models.CharField(max_length=140)
    file_url = models.CharField(max_length=999)
    created_by = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    category = models.CharField(max_length=140, choices=CIFAR100ImageClasses.choices)

    def __str__(self) -> str:
        return self.file_name
