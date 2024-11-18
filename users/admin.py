from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
@admin.register(User)   # 아래 CustomUserAdmin class가 user 모델을 관리할 것이라고 알려주기
class CustomUserAdmin(UserAdmin):
    pass