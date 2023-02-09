from rest_framework import serializers
from .image_classes import CIFAR100ImageClasses
from .models import Image


class ImageSerializer(serializers.Serializer):
    image_name = serializers.CharField(max_length=140)
    image = serializers.ImageField()
    created_by = serializers.CurrentUserDefault()
    created_at = serializers.DateTimeField(read_only=True)
    category = serializers.ChoiceField(choices=CIFAR100ImageClasses.choices)

    def create(self, validated_data):
        return Image.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.image_name = validated_data.get("image_name", instance.image_name)
        instance.image = validated_data.get("image", instance.image)
        instance.category = validated_data.get("category", instance.category)
        instance.save()
        return instance
