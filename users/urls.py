from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("me", views.Me.as_view()),
    path("create-account", views.CreateUser.as_view()),
    path("change-password", views.ChangePassword.as_view()),
    path("login", views.Login.as_view()),
    path("logout", views.Logout.as_view()),
    path(
        # auth token login takes up space in db while json web token login does not
        "token-login",
        obtain_auth_token,
    ),
    path("jwt-login", views.JWTLogin.as_view()),
]
