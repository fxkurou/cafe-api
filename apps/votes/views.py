from datetime import datetime

from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from votes.models import Vote
from votes.serializers import VoteSerializer
from menus.models import MenuItem, Menu


class VoteListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, restaurant_pk, menu_pk):
        votes = Vote.objects.filter(menu_item__menu_id=menu_pk)
        serializer = VoteSerializer(votes, many=True)
        return Response(serializer.data)

    def post(self, request, restaurant_pk, menu_pk):
        menu_item_id = request.data.get('menu_item_id')
        try:
            menu_item = MenuItem.objects.get(id=menu_item_id, menu_id=menu_pk)
        except MenuItem.DoesNotExist:
            return Response({"error": "Menu item not found"}, status=status.HTTP_404_NOT_FOUND)

        vote, created = Vote.objects.get_or_create(user=request.user, menu_item=menu_item)
        if created:
            return Response({"status": "vote counted"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "vote already exists"}, status=status.HTTP_200_OK)


class VoteCountForDayAPIView(APIView):
    def get(self, request, year, month, day):
        try:
            date = datetime(year, month, day).date()
        except ValueError:
            return Response({"error": "Invalid date format"}, status=status.HTTP_400_BAD_REQUEST)

        # Get all menus for the specified date
        menus = Menu.objects.filter(day=date)

        # Get all menu items for these menus
        menu_items = MenuItem.objects.filter(menu__in=menus)

        # Annotate the menu items with the vote count
        menu_items_with_votes = menu_items.annotate(vote_count=Count('votes'))

        # Serialize the data
        data = [
            {
                'menu_item': item.name,
                'description': item.description,
                'price': item.price,
                'vote_count': item.vote_count
            }
            for item in menu_items_with_votes
        ]

        return Response(data)