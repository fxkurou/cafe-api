from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Menu, MenuItem
from .permissions import IsStaffUser
from .serializers import MenuSerializer, MenuItemSerializer


class MenuListCreateAPIView(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated, IsStaffUser]
        else:
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    def get(self, request, restaurant_pk):
        menus = Menu.objects.filter(restaurant_id=restaurant_pk)
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

    def post(self, request, restaurant_pk):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(restaurant_id=restaurant_pk)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuDetailAPIView(APIView):
    def get_object(self, restaurant_pk, pk):
        try:
            return Menu.objects.get(restaurant_id=restaurant_pk, pk=pk)
        except Menu.DoesNotExist:
            return None

    def get(self, request, restaurant_pk, pk):
        menu = self.get_object(restaurant_pk, pk)
        if menu is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MenuSerializer(menu)
        return Response(serializer.data)

    def put(self, request, restaurant_pk, pk):
        menu = self.get_object(restaurant_pk, pk)
        if menu is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MenuSerializer(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, restaurant_pk, pk):
        menu = self.get_object(restaurant_pk, pk)
        if menu is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MenuItemListCreateAPIView(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated, IsStaffUser]
        else:
            self.permission_classes = [AllowAny]
        return super().get_permissions()
    def get(self, request, restaurant_pk, menu_pk):
        menu_items = MenuItem.objects.filter(menu_id=menu_pk)
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)

    def post(self, request, restaurant_pk, menu_pk):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(menu_id=menu_pk)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
