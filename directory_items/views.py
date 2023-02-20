from django.db import transaction
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_405_METHOD_NOT_ALLOWED
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import DirectoryItem
from .serializers import DirectoryItemSerializer


class UserFiles(APIView):
    permission_classes = [IsAuthenticated]

    def get_items_from_path(self, path):
        try:
            return DirectoryItem.objects.filter(path=path, created_by=self.request.user)
        except:
            raise NotFound

    def post(self, request):
        with transaction.atomic():
            path = request.data.get("path")
            folders_list = []
            images_list = []

            if path is None:
                return Response({"ok": False, "error": "Invalid path"})
            else:
                items = self.get_items_from_path(path)
                for item in items:
                    if item.path.split(".")[-1] == "":
                        folders_list.append(item)
                    else:
                        images_list.append(item)

                files = DirectoryItemSerializer(
                    images_list,
                    many=True,
                    context={"request": request},
                )
                folders = DirectoryItemSerializer(
                    folders_list,
                    many=True,
                    context={"request": request},
                )

            return Response({"folders": folders.data, "files": files.data})


class UploadFile(APIView):
    permission_classes = [IsAuthenticated]

    def is_file(self, path):
        return path.split(".")[-1] != ""

    def post(self, request):
        with transaction.atomic():
            if request.user.is_authenticated:
                serializer = DirectoryItemSerializer(data=request.data)
                if serializer.is_valid():
                    new_image = serializer.save(created_by=request.user)
                    return Response(
                        {
                            "ok": True,
                            "data": DirectoryItemSerializer(new_image).data,
                        },
                    )
                else:
                    return Response({"ok": False, "error": serializer.errors})
            else:
                return Response(HTTP_405_METHOD_NOT_ALLOWED)
