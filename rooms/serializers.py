from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Amenity, Room
from users.serializer import TinyUserSerializer
from reviews.serializers import ReviewSerializer
from categories.serializer import CategorySerializer
from medias.serializers import PhotoSerializer

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description"
        )

class RoomDetailSerializer(serializers.ModelSerializer):

    owner = TinyUserSerializer(read_only=True)    # depth = 1 사용하지 않고, user에 serializer 파일 생성 후, 필요한 부분만 가져옴
    # amenities = AmenitySerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.SerializerMethodField()    # rating 계산할 method를 만들 예정
    is_owner = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)
    # reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        exclude = ("amenities",)
        # fields = "__all__"
        # depth = 1           # object ID만 표시하지 않고, object의 모든 것을 보여주게 됨... but, password처럼 개인 정보들도 다 보여주기 때문에 보안 필요

    def get_rating(self, room):     # customized.. 유저가 요청한 데이터를 계산해서 필드로 만들어야 할 때..      형태 중요
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user
        
    # def create(self, validated_data):
    #     return 

class RoomListSerializer(serializers.ModelSerializer):

    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_owner",
            "photos",
        )

    def get_rating(self, room):
        return room.rating()
    
    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user