import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(email='user@example.com', password='password123', first_name='John', last_name='Doe')
    assert user.email == 'user@example.com'
    assert user.check_password('password123')
    assert user.first_name == 'John'
    assert user.last_name == 'Doe'
    assert not user.is_staff
    assert not user.is_superuser


@pytest.mark.django_db
def test_create_superuser():
    user = User.objects.create_superuser(email='admin@example.com', password='password123', first_name='Admin', last_name='User')
    assert user.email == 'admin@example.com'
    assert user.check_password('password123')
    assert user.first_name == 'Admin'
    assert user.last_name == 'User'
    assert user.is_staff
    assert user.is_superuser


@pytest.mark.django_db
def test_user_str():
    user = User.objects.create_user(email='user@example.com', password='password123', first_name='John', last_name='Doe')
    assert str(user) == 'John Doe'
