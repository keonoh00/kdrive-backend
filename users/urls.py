from django.urls import path
from . import views

urlpatterns = [
    path("me", views.Me.as_view()),
    path("create-user", views.CreateUser.as_view()),
    path("change-password", views.ChangePassword.as_view()),
    path("login", views.Login.as_view()),
    path("logout", views.Logout.as_view()),
]
