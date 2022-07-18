import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_id() :
    user = create_user()
    assert  user.id == 1


def create_user():
    '''create a user'''
    payload = dict(
        name="Khaled",
        username="khaledblb@gmaill.com",
        password="Aa123456"
    )
    user = User.objects.create_user(payload)

    return user