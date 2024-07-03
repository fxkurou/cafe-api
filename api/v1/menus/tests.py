import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from api.v1.users.models import User
from api.v1.restaurants.models import Restaurant
from api.v1.menus.models import Menu


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user(db):
    user = User.objects.create_user(email='user@example.com', password='password123', first_name='John', last_name='Doe')
    return user


@pytest.fixture
def create_staff_user(db):
    user = User.objects.create_user(email='staff@example.com', password='password123', first_name='Staff', last_name='Member', is_staff=True)
    return user


@pytest.fixture
def authenticate_user(api_client, create_user):
    api_client.force_authenticate(user=create_user)
    return api_client


@pytest.fixture
def authenticate_staff_user(api_client, create_staff_user):
    api_client.force_authenticate(user=create_staff_user)
    return api_client


@pytest.fixture
def create_restaurant(create_staff_user):
    return Restaurant.objects.create(name='Test Restaurant', owner=create_staff_user)


def test_create_menu(authenticate_staff_user, create_restaurant):
    url = reverse('menu-list', kwargs={'restaurant_pk': create_restaurant.pk})
    response = authenticate_staff_user.post(url, {
        'day': '2024-07-01',
        'restaurant': create_restaurant.pk
    })
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['day'] == '2024-07-01'


def test_get_menu_detail(authenticate_user, create_restaurant):
    menu = Menu.objects.create(restaurant=create_restaurant, day='2024-07-01')
    url = reverse('menu-detail', kwargs={'restaurant_pk': create_restaurant.pk, 'pk': menu.pk})
    response = authenticate_user.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['day'] == '2024-07-01'
