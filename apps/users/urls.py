from django.urls import path

from users.views import BaserProfileObtainToken
from users.views import UserRegisterView

urlpatterns = [
    path("token/", BaserProfileObtainToken.as_view(), name="login"),
    path("register/", UserRegisterView.as_view(), name="register"),
]