from rest_framework import serializers
from users.serializer import TinyUserSerializer
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = (
            "user",
            "payload",
            "rating",
        )