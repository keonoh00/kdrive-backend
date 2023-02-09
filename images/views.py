from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from .models import Image
from .serializers import ImageSerializer


class UploadImage(APIView):
    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            new_image = serializer.save()
            return Response(
                {
                    "ok": True,
                    "data": {ImageSerializer(new_image).data},
                },
            )
        else:
            return Response({"ok": False, "error": serializer.errors})


class Image(APIView):
    def get_object(self, pk):
        try:
            image = Image.objects.get(id=pk)
            self.image = image
        except:
            raise NotFound

    def get(self, _, pk):
        serializer = ImageSerializer(self.get_object(pk))
        return Response(
            {
                "ok": True,
                "data": serializer.data,
            },
        )

    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            new_image = serializer.save()
            return Response(
                {
                    "ok": True,
                    "data": {ImageSerializer(new_image).data},
                },
            )
        else:
            return Response({"ok": False, "error": serializer.errors})

    def put(self, request, pk):
        serializer = ImageSerializer(
            self.get_object(pk),
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_data = serializer.save()
            return Response(
                {
                    "ok": True,
                    "data": updated_data,
                },
            )
        else:
            return Response({"ok": False, "error": serializer.errors})

    def delete(self, _, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)


""" Below is the legacy code"""

# @api_view(["POST"])
# def upload(request):
#     match request.method:
#         case "POST":
#             serializer = ImageSerializer(data=request.data)
#             if serializer.is_valid():
#                 new_image = serializer.save()
#                 return Response(
#                     {
#                         "ok": True,
#                         "data": {ImageSerializer(new_image).data},
#                     },
#                 )
#             else:
#                 return Response({"ok": False, "error": serializer.errors})

#         case _:
#             return Response(status=HTTP_405_METHOD_NOT_ALLOWED)


# @api_view(["GET", "PUT", "DELETE"])
# def image(request, pk):
#     try:
#         image = Image.objects.get(id=pk)
#     except:
#         raise NotFound

#     match request.method:
#         case "GET":
#             serializer = ImageSerializer(image)
#             return Response(
#                 {
#                     "ok": True,
#                     "data": serializer.data,
#                 },
#             )

#         case "PUT":
#             serializer = ImageSerializer(
#                 image,
#                 data=request.data,
#                 partial=True,
#             )
#             if serializer.is_valid():
#                 updated_data = serializer.save()
#                 return Response(
#                     {
#                         "ok": True,
#                         "data": updated_data,
#                     },
#                 )
#             else:
#                 return Response({"ok": False, "error": serializer.errors})

#         case "DELETE":
#             image.delete()
#             return Response(status=HTTP_204_NO_CONTENT)

#         case _:
#             return Response(status=HTTP_405_METHOD_NOT_ALLOWED)
