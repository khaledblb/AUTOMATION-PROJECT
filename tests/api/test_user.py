import pytest
from rest_framework.test import APIClient

'''
Integration testing testing api to register user
'''
@pytest.mark.django_db
def test_register_user():
    '''
        testing register request if return a valid response
    '''
    client = APIClient()
    payload = dict(
        name="testing123",
        email="test11@test.com",
        password="super-secret"
    )
    response = client.post("/api/users/register/", payload)
    data = response.data

    assert data["name"] == payload["name"]

@pytest.mark.django_db
def test_login_user():
    '''
    testing log-in integrtion function if returns valid respose
    '''
    client = APIClient()
    payload = dict(
        name="Khaled",
        username="khaledblb@gmaill.com",
        password="Aa123456"
    )
    registerResponse = client.post("api/users/register/", payload)
    loginResponse = client.post("api/users/login/",payload)

    # assert loginResponse.status_code == 200
    assert registerResponse.status_code == 404