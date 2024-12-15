from django.urls import path
from .views import WishLists, WishlistDetail, WishlistToggle

urlpatterns = [
    path("", WishLists.as_view()),
    path("<int:pk>", WishlistDetail.as_view()),
    path("<int:pk>/rooms/<int:pk>", WishlistToggle.as_view()),
]