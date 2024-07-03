from django.urls import path
from api.v1.votes.views import VoteListCreateAPIView, VoteCountForDayAPIView

urlpatterns = [
    path('restaurants/<int:restaurant_pk>/menus/<int:menu_pk>/votes/', VoteListCreateAPIView.as_view(),
         name='vote-list'),
    path('votes/<int:year>/<int:month>/<int:day>/', VoteCountForDayAPIView.as_view(), name='votes-for-day'),
]