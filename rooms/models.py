from django.db import models
from common.models import CommonModel 

# Create your models here.
class Room(CommonModel):

    """Room Model Definition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = "shared_room", "Shared Room"

    name = models.CharField(max_length=180, default="")
    country = models.CharField(max_length=50, default="South Korea")
    city = models.CharField(max_length=80, default="Seoul")
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    pet_friendly = models.BooleanField(default=True)
    kind = models.CharField(max_length=20, choices=RoomKindChoices.choices)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="rooms")     # related_name="rooms"   :  room_set을 rooms로 대체하여 보여줌, ORM 활용 시 유용
    amenities = models.ManyToManyField("rooms.Amenity", related_name="rooms")
    category = models.ForeignKey("categories.Category", null=True, blank=True, on_delete=models.SET_NULL, related_name="rooms")
    # created_at = models.DateTimeField(auto_now_add=True)       # auto_now_add : 해당 object가 처음 생성됐을 때의 시간으로 설정.. Room 생성될 때마다
    # updated_at = models.DateTimeField(auto_now=True)           # auto_now :     해당 object가 저장될 때마다 현재 date로 설정... Room 업데이트할 때마다

    def __str__(room) -> str:
        return room.name
    
    def total_amenities(room):
        return room.amenities.count()
    
    def rating(room):
        count = room.reviews.count()
        if count == 0:
            return 0
        else:
            total_rating = 0
            for review in room.reviews.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating / count, 2)    # 소수점 2자리까지


class Amenity(CommonModel):     # 공용으로 사용하기로 한 CommonModel을 상속받음

    """Amenity Definition"""

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, default="", blank=True)
        
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Amenities"       # title 수정 : Amenitys -> Amenities
        
