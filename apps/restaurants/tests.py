import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from users.models import User
from restaurants.models import Restaurant


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


def test_get_restaurant_detail(authenticate_user, create_user):
    restaurant = Restaurant.objects.create(name='Test Restaurant', owner=create_user)
    url = reverse('restaurant-detail', kwargs={'pk': restaurant.pk})
    response = authenticate_user.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == 'Test Restaurant'
