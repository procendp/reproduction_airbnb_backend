from django.db import models

# Create your models here.
class House(models.Model):

    """"Model Definition for Houses"""

    name = models.CharField(max_length=140)    # DB에 있는 House는 name을 가질거고, 이 형식은 최대 길이 140자의 텍스트형
    price = models.PositiveIntegerField()
    description = models.TextField()           # CharField 보다 긴 글 작성 시 사용
    address = models.CharField(max_length=140)
