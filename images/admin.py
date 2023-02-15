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
        "category",
        "created_by",
        "created_at",
    )

    list_filter = (
        "category",
        "created_by",
        "created_at",
    )

    search_fields = (
        "image_name",
        "=created_by__username",
        "=category",
    )

    readonly_fields = ("created_at", "updated_at")

    pass
