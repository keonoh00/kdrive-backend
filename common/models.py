from django.db import models


class CommonModel(models.Model):
    """Common Model Definitions"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # abstract makes this model not to be created in the database
        abstract = True
