from rest_framework import serializers
from .models import DirectoryItem
from users.serializers import PublicUserSerializer


class DirectoryItemSerializer(serializers.ModelSerializer):
    created_by = PublicUserSerializer(read_only=True)

    class Meta:
        model = DirectoryItem
        fields = "__all__"
