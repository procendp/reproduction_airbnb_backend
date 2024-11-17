from django.contrib import admin
from .models import House

# Register your models here.

@admin.register(House)      # decorator : HouseAdmin class가 House model(models.py에 만든 class)을 통제할 것    # http://127.0.0.1:8000/admin/ 에 Houses 패널 추가됨    # admin을 커스텀하고 싶다면 이렇게 이용하면 됨
class HouseAdmin(admin.ModelAdmin):
    #pass    # class 전체를 상속함, 수정하지 않음..  수정 없으니 ModelAdmin 그 자체라고 봐도 됨

    list_display = (
        # culumn in admin
        "name",
        "price_per_night",
        "address",
        "pet_allowed"
    )

    list_filter = ("price_per_night", "pet_allowed")
    search_fields = ("address",)  # list[]가 아닌 tuple() 사용할 때, 원소가 1개라면 뒤에 ,(comma) 붙여줘야함
    # exclude = ("price_per_night",)   # admin 페이지에서 price 수정을 막고 싶다면, 이를 통해 웹 상에서 감춤

# 하지만 admin 패널에 House를 생성해도 DB에선 아직 모름 -> Migration 가서 처리해줘야함
