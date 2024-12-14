from django.db import models
from common.models import CommonModel

# Create your models here.
class Photo(CommonModel):

    file = models.URLField()        # 보안 위해 URLField로 대체
    # file = models.ImageField()
    description = models.CharField(max_length=140)
    room = models.ForeignKey("rooms.Room", null=True, blank=True, on_delete=models.CASCADE, related_name="photos")
    experience = models.ForeignKey("experiences.Experience", null=True, blank=True, on_delete=models.CASCADE, related_name="photos")

    def __str__(self):
        return "Photo File"

class Video(CommonModel):

    file = models.URLField()
    # file = models.FileField()
    experience = models.OneToOneField("experiences.Experience", on_delete=models.CASCADE,related_name="videos" )

    def __str__(self):
        return "Video File"