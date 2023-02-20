from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserFiles.as_view()),
    path("upload", views.UploadFile.as_view()),
]
