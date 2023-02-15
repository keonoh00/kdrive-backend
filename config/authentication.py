from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
import jwt
from users.models import User


# This is a custom authentication class that will be used to authenticate
# However, this is not a good way to authenticate users, as it is not secure
class TrustMeBroAuth(BaseAuthentication):
    def authenticate(self, request):
        username = request.headers.get("trust-me-bro")
        if not username:
            return None

        try:
            user = User.objects.get(username=username)
            return (user, None)

        except User.DoesNotExist:
            raise AuthenticationFailed("No such user: " + username)


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("JWT")
        if not token:
            return None

        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        if not payload:
            raise AuthenticationFailed("Invalid token")

        try:
            user = User.objects.get(pk=payload.get("pk"))
            return (user, None)
        except:
            raise AuthenticationFailed("User not found")
