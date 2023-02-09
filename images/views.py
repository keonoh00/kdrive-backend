from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_405_METHOD_NOT_ALLOWED
from .models import Image
from .serializers import ImageSerializer


@api_view(["POST"])
def upload(request):
    match request.method:
        case "POST":
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

        case _:
            return Response(status=HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET", "PUT", "DELETE"])
def image(request, pk):
    try:
        image = Image.objects.get(id=pk)
    except:
        raise NotFound

    match request.method:
        case "GET":
            serializer = ImageSerializer(image)
            return Response(
                {
                    "ok": True,
                    "data": serializer.data,
                },
            )

        case "PUT":
            serializer = ImageSerializer(
                image,
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

        case "DELETE":
            image.delete()
            return Response(status=HTTP_204_NO_CONTENT)

        case _:
            return Response(status=HTTP_405_METHOD_NOT_ALLOWED)
