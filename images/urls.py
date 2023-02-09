from django.urls import path
from . import views

urlpatterns = [
    path("", views.UploadImage.as_view()),
    path("<int:pk>", views.Image.as_view()),
]
