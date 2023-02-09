from rest_framework import serializers
from .image_classes import CIFAR100ImageClasses
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            "image_name",
            "image",
            "category",
        )
        """ Or we can use exclude instead of fields: """
        # exclude = (
        #     "created_by",
        #     "created_at",
        # )

        """ If all fields should be editable, use the following code: """
        # fields = "__all__"


"""Using Serializer"""

# class ImageSerializer(serializers.Serializer):
#     image_name = serializers.CharField(max_length=140)
#     image = serializers.ImageField()
#     created_by = serializers.CurrentUserDefault()
#     created_at = serializers.DateTimeField(read_only=True)
#     category = serializers.ChoiceField(choices=CIFAR100ImageClasses.choices)

#     def create(self, validated_data):
#         return Image.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.image_name = validated_data.get("image_name", instance.image_name)
#         instance.image = validated_data.get("image", instance.image)
#         instance.category = validated_data.get("category", instance.category)
#         instance.save()
#         return instance
