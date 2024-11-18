from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):   # models.Model 상속 받지 않은 이유 : User를 처음부터 다 만드려는 건데, 그럴 이유 없으니 사용 안함, django가 다 가지고 있음

    # first_name과 last_name을 쓰지 않을 계획임. -> django 내 소스를 수정하지말고, 여기서 오버라이딩 한번 해주면서 숨겨주자
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    name = models.CharField(max_length=150, default="")         # 기본 값 설정해줘야함, 기존에 등록돼있던 유저들에게도 컬럼을 부여하는데, 뭘 부여할지 django는 모르잖아
    is_host = models.BooleanField(default=False)     # null=True : T, F 가 아닌 Null로 채우기