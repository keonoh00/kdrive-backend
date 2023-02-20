from django.contrib import admin
from .models import DirectoryItem


@admin.register(DirectoryItem)
class DirectoryItemAdmin(admin.ModelAdmin):

    """DirectoryItem Admin Definition"""

    list_display = (
        "name",
        "created_by",
        "created_at",
    )

    list_filter = (
        "created_by",
        "created_at",
    )

    pass
