from django.db import models
from common.models import CommonModel
from .image_classes import CIFAR100ImageClasses


class Image(CommonModel):

    """Image Model Definition"""

    image_name = models.CharField(max_length=140, default="")
    image = models.ImageField()
    created_by = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="images",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    category = models.CharField(max_length=140, choices=CIFAR100ImageClasses.choices)

    def __str__(self) -> str:
        return self.file_name

    class Meta:
        # verbose_name_plural manually sets the plural form of the model name
        verbose_name_plural = "Images"
