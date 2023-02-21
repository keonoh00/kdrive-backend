from django.db import models
from common.models import CommonModel


class DirectoryItem(CommonModel):

    """DirectoryItem Model Definition"""

    name = models.CharField(max_length=140)
    image_url = models.URLField(null=True)
    created_by = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="files",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    path = models.CharField(max_length=1000, default="/")

    def __str__(self) -> str:
        return self.name
