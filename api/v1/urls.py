from django.urls import path
from restaurants.views import RestaurantListCreateAPIView, RestaurantDetailAPIView
from menus.views import MenuListCreateAPIView, MenuDetailAPIView, MenuItemListCreateAPIView
from votes.views import VoteListCreateAPIView, VoteCountForDayAPIView

from users.views import BaserProfileObtainToken, UserRegisterView

urlpatterns = [
    path('restaurants/', RestaurantListCreateAPIView.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantDetailAPIView.as_view(), name='restaurant-detail'),

    path('restaurants/<int:restaurant_pk>/menus/', MenuListCreateAPIView.as_view(), name='menu-list'),
    path('restaurants/<int:restaurant_pk>/menus/<int:pk>/', MenuDetailAPIView.as_view(), name='menu-detail'),

    path('restaurants/<int:restaurant_pk>/menus/', MenuListCreateAPIView.as_view(), name='menu-list'),
    path('restaurants/<int:restaurant_pk>/menus/<int:pk>/', MenuDetailAPIView.as_view(), name='menu-detail'),
    path('restaurants/<int:restaurant_pk>/menus/<int:menu_pk>/items/', MenuItemListCreateAPIView.as_view(), name='menu-item-list'),

    path('restaurants/<int:restaurant_pk>/menus/<int:menu_pk>/votes/', VoteListCreateAPIView.as_view(), name='vote-list'),
    path('votes/<int:year>/<int:month>/<int:day>/', VoteCountForDayAPIView.as_view(), name='votes-for-day'),

    path("token/", BaserProfileObtainToken.as_view(), name="login"),
    path("register/", UserRegisterView.as_view(), name="register"),
]
