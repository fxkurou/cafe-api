from django.urls import path

from api.v1.users.views import BaserProfileObtainToken
from api.v1.users.views import UserRegisterView

urlpatterns = [
    path("token/", BaserProfileObtainToken.as_view(), name="login"),
    path("register/", UserRegisterView.as_view(), name="register"),
]