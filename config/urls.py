from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/v1/restaurants/', include('restaurants.urls')),
    path('api/v1/', include('menus.urls')),
    path('api/v1/', include('votes.urls')),
]
