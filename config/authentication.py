from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
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
