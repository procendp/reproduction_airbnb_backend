from django.urls import path
from .views import PhotoDetail, GetUploadURL
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("photos/get-url", GetUploadURL.as_view()),
    path("photos/<int:pk>",PhotoDetail.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)