import pytest
from rest_framework.test import APIClient
from rest_framework.authtoken.admin import User
# Api test  - Integration testing

@pytest.mark.django_db
def test_api_create_product():
    '''
    Api test: create a product
    these test check if create product request return valid response
    '''
    client = APIClient()
    super_user = User.objects.create_superuser(username='testuser',password='134')
    client.force_authenticate(super_user)
    response = client.post("/api/products/create/")

    assert response.status_code == 200

