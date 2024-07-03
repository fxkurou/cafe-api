from django.urls import path, include


urlpatterns = [
    path('restaurants/', include('api.v1.restaurants.urls')),
    path('restaurants/<int:restaurant_pk>/menus/', include('api.v1.menus.urls')),
    path('', include('api.v1.votes.urls')),
    path('users/', include('api.v1.users.urls')),
]
