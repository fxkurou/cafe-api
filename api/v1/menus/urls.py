from django.urls import path
from api.v1.menus.views import MenuListCreateAPIView, MenuDetailAPIView, MenuItemListCreateAPIView

urlpatterns = [
    path('', MenuListCreateAPIView.as_view(), name='menu-list'),
    path('<int:pk>/', MenuDetailAPIView.as_view(), name='menu-detail'),
    path('<int:menu_pk>/items/', MenuItemListCreateAPIView.as_view(), name='menu-item-list'),
]