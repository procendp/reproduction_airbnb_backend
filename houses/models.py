from django.db import models

# Create your models here.
class House(models.Model):

    """"Model Definition for Houses"""

    name = models.CharField(max_length=140)    # DB에 있는 House는 name을 가질거고, 이 형식은 최대 길이 140자의 텍스트형
    price_per_night = models.PositiveIntegerField(verbose_name="Price", help_text="Positive Numbers Only")     # verbose_name : 웹 상에서의 표기 정의
    description = models.TextField()           # CharField 보다 긴 글 작성 시 사용
    address = models.CharField(max_length=140)
    pet_allowed = models.BooleanField(default=True, help_text="Does this house allow pets?")

    def __str__(self):
        return self.name    # admin 패널 내 House object(1) 표시 수정
