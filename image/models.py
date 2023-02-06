from django.db import models


class Image(models.Model):
    """Model definition for Image"""

    name = models.CharField(max_length=140)
    file_URL = models.TextField()
    category = models.CharField(max_length=140)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    created_by = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
