import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from api.v1.users.models import User
from api.v1.restaurants.models import Restaurant
from api.v1.menus.models import Menu, MenuItem
from api.v1.votes.models import Vote
from datetime import date


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


@pytest.fixture
def create_menu(create_restaurant):
    return Menu.objects.create(restaurant=create_restaurant, day=date.today())


@pytest.fixture
def create_menu_item(create_menu):
    return MenuItem.objects.create(menu=create_menu, name='Item1', description='Description1', price='10.00')


def test_create_vote(authenticate_user, create_menu_item):
    url = reverse('vote-list', kwargs={'restaurant_pk': create_menu_item.menu.restaurant.pk, 'menu_pk': create_menu_item.menu.pk})
    response = authenticate_user.post(url, {'menu_item_id': create_menu_item.id})
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['status'] == 'vote counted'


def test_votes_for_day(authenticate_user, create_menu_item):
    menu_item = create_menu_item
    Vote.objects.create(user=menu_item.menu.restaurant.owner, menu_item=menu_item)
    url = reverse('votes-for-day', kwargs={'year': menu_item.menu.day.year, 'month': menu_item.menu.day.month, 'day': menu_item.menu.day.day})
    response = authenticate_user.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['menu_item'] == menu_item.name
    assert response.data[0]['vote_count'] == 1
