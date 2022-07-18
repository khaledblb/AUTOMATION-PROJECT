import pytest
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.test import APIClient
from base.models import Product

@pytest.mark.django_db
def test_register_user():
    client = APIClient()
    payload = dict(
        name="Khaled",
        email="khaledblb@test.com",
        password="123123"
    )

    response = client.post("/api/users/register/", payload)
    data = response.data

    assert data["name"] == payload["name"]
    return data

@pytest.fixture()
def user_1(db):
    return User.objects.create_user("test-user")

@pytest.mark.django_db
def test_delete_user(admin_user) :
    client = APIClient()
    # response = client.delete(user_1)
    response = client.post("/api/users/delete/",user_1)

    assert response.status_code == 200
