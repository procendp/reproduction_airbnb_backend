from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views
urlpatterns = [
    path("", views.Users.as_view()),
    path("me", views.Me.as_view()),
    path("change-password", views.ChangePassword.as_view()),
    path("log-in", views.LogIn.as_view()),                      # How to Log-in (1) : Cookie log-in
    path("log-out", views.LogOut.as_view()),
    path("token-login", obtain_auth_token),                     # How to Log-in (2) :  Auth Token log-in --> username과 password를 보내면 token 반환
    path("jwt-login", views.JWTLogIn.as_view()),                #  How to Log-in (3) : JWT Log-in
    path("@<str:username>", views.PublicUser.as_view()),
]