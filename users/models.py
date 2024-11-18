from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):   # models.Model 상속 받지 않은 이유 : User를 처음부터 다 만드려는 건데, 그럴 이유 없으니 사용 안함, django가 다 가지고 있음
    pass