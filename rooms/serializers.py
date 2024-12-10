from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room
from users.serializer import TinyUserSerializer
from categories.serializer import CategorySerializer

class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description"
        )

class RoomDetailSerializer(ModelSerializer):

    owner = TinyUserSerializer(read_only=True)    # depth = 1 사용하지 않고, user에 serializer 파일 생성 후, 필요한 부분만 가져옴
    amenities = AmenitySerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Room
        fields = "__all__"
        # depth = 1           # object ID만 표시하지 않고, object의 모든 것을 보여주게 됨... but, password처럼 개인 정보들도 다 보여주기 때문에 보안 필요
        
    # def create(self, validated_data):
    #     return 

class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price"
        )