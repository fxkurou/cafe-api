from django.urls import path
from menus.views import MenuListCreateAPIView, MenuDetailAPIView, MenuItemListCreateAPIView

urlpatterns = [
    path('restaurants/<int:restaurant_pk>/menus/', MenuListCreateAPIView.as_view(), name='menu-list'),
    path('restaurants/<int:restaurant_pk>/menus/<int:pk>/', MenuDetailAPIView.as_view(), name='menu-detail'),
    path('restaurants/<int:restaurant_pk>/menus/<int:menu_pk>/items/', MenuItemListCreateAPIView.as_view(), name='menu-item-list'),
]