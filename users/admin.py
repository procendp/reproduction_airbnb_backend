from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
@admin.register(User)   # 아래 CustomUserAdmin class가 user 모델을 관리할 것이라고 알려주기
class CustomUserAdmin(UserAdmin):
    fieldsets = (       # fieldsets : field를 나눈 layer 그대로 표현해줌,    tuple 꼭!
        (
            "profile", 
            {
                "fields": (
                    "avatar",
                    "username", 
                    "password", 
                    "name", 
                    "email", 
                    "is_host",
                    "gender",
                    "language",
                    "currency",
                    ),
            },
        ),
        (
            "permissions", 
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    ),

                "classes": ("collapse",),
            },
        ),
        (
            "Important dates",
            {
                "fields": (
                    "last_login", 
                    "date_joined"
                    ),
                
                "classes": ("collapse",),   # [보기] 속으로 들어감
            },
        ),
    )

    list_display = ("username", "email", "name", "is_host")


