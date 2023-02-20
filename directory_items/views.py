import requests
import paramiko
from django.db import transaction
from django.conf import settings
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAcceptable
from rest_framework.status import (
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_201_CREATED,
    HTTP_202_ACCEPTED,
)
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
                return Response({"path": "path is required"})
            else:
                items = self.get_items_from_path(path)
                for item in items:
                    if item.name.split("/")[-1] == "":
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

    def is_folder(self, path):

        return path.split("/")[-1] == ""

    def post(self, request):
        with transaction.atomic():
            if request.user.is_authenticated:
                name = request.data.get("name")
                image_url = request.data.get("image_url")
                is_folder = self.is_folder(name)
                # TODO: Classification here
                if is_folder and image_url:
                    return Response(
                        {"error": "Folder can't have image_url"},
                        status=HTTP_400_BAD_REQUEST,
                    )
                if not is_folder and not image_url:
                    return Response(
                        {"error": "File must have image_url"},
                        status=HTTP_400_BAD_REQUEST,
                    )
                serializer = DirectoryItemSerializer(data=request.data)
                if serializer.is_valid():
                    new_image = serializer.save(created_by=request.user)
                    return Response(
                        {
                            "ok": True,
                            "data": DirectoryItemSerializer(new_image).data,
                        },
                        status=HTTP_201_CREATED,
                    )
                else:
                    return Response({"ok": False, "error": serializer.errors})
            else:
                return Response(
                    {"error": "Not authorized"},
                    status=HTTP_401_UNAUTHORIZED,
                )


class SingleFile(APIView):
    permission_classes = [IsAuthenticated]

    def get_file(self, pk):
        try:
            return DirectoryItem.objects.get(pk=pk, created_by=self.request.user)
        except:
            raise NotFound

    def get(self, request, pk):
        file = self.get_file(pk)
        serializer = DirectoryItemSerializer(file)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response({"ok": False, "error": serializer.errors})

    def put(self, request, pk):
        file = self.get_file(pk)
        serializer = DirectoryItemSerializer(file, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        else:
            return Response(
                {"ok": False, "error": serializer.errors},
                status=HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        file = self.get_file(pk)
        try:
            file.delete()
            return Response(
                {"ok": True, "message": "File deleted"},
                status=HTTP_204_NO_CONTENT,
            )
        except:
            return Response(
                {"ok": False, "error": "File not deleted"},
                status=HTTP_400_BAD_REQUEST,
            )


class GetUploadURL(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        url = f"https://api.cloudflare.com/client/v4/accounts/{settings.CF_ACCOUNT_ID}/images/v2/direct_upload"
        response = requests.post(
            url,
            headers={
                "Authorization": f"Bearer {settings.CF_API_TOKEN}",
            },
        )

        one_time_url = response.json().get("result").get("uploadURL")
        cf_image_id = response.json().get("result").get("id")

        return Response(
            {"uploadURL": one_time_url, "id": cf_image_id}, status=HTTP_201_CREATED
        )


class Classification(APIView):
    def get(self, request):

        cli = paramiko.SSHClient()
        cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        cli.connect(
            settings.GPU_SERVER_ADDRESS,
            username=settings.GPU_SERVER_USERNAME,
            password=settings.GPU_SERVER_PASSWORD,
        )

        _, stdout, _ = cli.exec_command("ls -la")
        for line in stdout:
            print(line.strip("\n"))

        cli.close()

        return Response({"ok": True, "message": "Classification endpoint"})
