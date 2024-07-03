from django.urls import path
from restaurants.views import RestaurantListCreateAPIView, RestaurantDetailAPIView

urlpatterns = [
    path('', RestaurantListCreateAPIView.as_view(), name='restaurant-list'),
    path('<int:pk>/', RestaurantDetailAPIView.as_view(), name='restaurant-detail'),
]