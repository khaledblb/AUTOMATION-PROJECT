import pytest
from django.contrib.auth.models import User
'''
Unit tests -> checking user creation func
'''
@pytest.fixture()
def user_1(db):
    return User.objects.create_user("test-user")

@pytest.mark.django_db
def test_user_create_by_DB_count():
    User.objects.create_user('test','test@test.com','test')
    count = User.objects.all().count()
    assert count == 1


@pytest.mark.django_db
def test_create_user_by_id() :
    payload = dict(
        name="Khaled",
        username="khaledblb@gmaill.com",
        password="Aa123456"
    )
    user = User.objects.create_user(payload)

    assert  user.id == 1

@pytest.mark.django_db
def test_create_user_by_status_IsActive():
    payload = dict(
        name="Khaled",
        username="khaledblb@gmaill.com",
        password="Aa123456"
    )
    user = User.objects.create_user(payload)

    assert user.is_active == True

@pytest.mark.django_db
def test_create_user_by_name_field():
    payload = dict(
        name= "Khaled",
        username= "khaledblb@gmaill.com",
        password= "Aa123456"
    )
    user = User.objects.create_user(payload)

    assert user.username['name'] == payload['name']

