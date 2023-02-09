from django.contrib import admin
from .models import Image


@admin.action(description="Mark selected images as verified")
def make_verified(modeladmin, request, queryset):
    # one way to update the queryset
    # queryset.update(verified=True)

    # another way to update the queryset
    for image in queryset:
        image.verified = True
        image.save()


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    """Image Admin Definition"""

    actions = [make_verified]

    list_display = (
        "image_name",
        "created_at",
        "created_by",
        "category",
    )

    list_filter = (
        "created_at",
        "created_by",
        "category",
    )

    search_fields = (
        "image_name",
        "=created_by__username",
        "=category",
    )

    readonly_fields = ("created_at", "image", "updated_at")

    pass
