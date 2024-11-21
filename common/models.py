from django.db import models

# 공통으로 가지고 있는 것들 담아줄 곳
# DB에 들어갈 것은 아님, 다른 model들의 설계도 용도

class CommonModel(models.Model):

    """Common Model Definition"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True     # : 다른 application에서 재사용 가능!... 따라서 django가 이걸 보면 DB에 저장 안함