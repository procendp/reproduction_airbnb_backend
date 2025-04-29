from rest_framework.serializers import ModelSerializer
from .models import User

class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "avatar",
            "username"
        )

class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "id",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
        )

class SignUpSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "name",
            "password",
            "gender",
            "language",
            "currency",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "gender": {"required": True},
            "language": {"required": True},
            "currency": {"required": True},
        }