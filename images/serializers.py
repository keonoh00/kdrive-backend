from rest_framework import serializers
from .image_classes import CIFAR100ImageClasses
from .models import Image
from users.serializers import PublicUserSerializer


class ImageSerializer(serializers.ModelSerializer):
    created_by = PublicUserSerializer(read_only=True)

    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Image

        """
        If all fields should be editable, use the following code: 
        "created_at", "updated_at" will be read-only
        """
        fields = "__all__"

        """Other option"""
        # fields = (
        #     "image_name",
        #     "image",
        #     "category",
        # )
        """ Or we can use exclude instead of fields: """
        # exclude = (
        #     "created_by",
        #     "created_at",
        # )

    def get_is_owner(self, obj):
        request = self.context.get("request")
        if request.user.is_authenticated:
            return obj.owner == request.user
        return False


"""Using normal Serializer"""

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
