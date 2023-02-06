from django.contrib import admin
from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("name", "file_URL", "category", "created_at")
    list_filter = ("name", "category", "created_at")
    search_fields = ("name",)
