from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserFiles.as_view()),
    path("generate-upload-url", views.GetUploadURL.as_view()),
    path("upload", views.UploadFile.as_view()),
    path("<int:pk>", views.SingleFile.as_view()),
]
