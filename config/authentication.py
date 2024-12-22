#### users/views.py 보다 빠르게 확인할 곳

import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from users.models import User

class JWTAuthentication(BaseAuthentication):
    
    def authenticate(self, request):
        token = request.headers.get("jwt")
        if not token:
            return None
        
        decoded = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=["HS256"],
        )
        pk = decoded.get("pk")
        if not pk:
            raise AuthenticationFailed("Invalid token")
        try:
            user = User.objects.get(pk=pk)
            return (user, None)
        except User.DoesNotExist:
            raise AuthenticationFailed("User Not Found")






# class TrustMeAuthentication(BaseAuthentication):        # 좋지 않음.. user 아무나 넣어도 다 입력함
#     def authenticate(self, request):
#         username = request.headers.get("Trust-Me")
#         if not username:
#             return None
#         try:
#             user = User.objects.get(username=username)
#             return (user, None)
#         except User.DoesNotExist:
#             raise AuthenticationFailed(f"No user {username}")