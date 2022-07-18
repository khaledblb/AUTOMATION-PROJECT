from rest_framework.authtoken.admin import User
from rest_framework.test import APIClient
import pytest
from base.models import Product

from django.contrib.auth.models import User

@pytest.mark.django_db
def test_upload_product ():
    pass
    # client = APIClient()
    #
    # # user = User.objects.create_user("admin","admin@gmail.com","gagishmagi")
    # user = User.objects.create_superuser("admin","admin@gmail.com","gagishmagi")
    # product = Product.objects.create(
    #     user=admin_user,
    #     name=" Product Name ",
    #     price=0,
    #     brand="Sample brand ",
    #     countInStock=0,
    #     category="Sample category",
    #     description=" "
    # )
    #
    # response = client.post("/api/products/create/",product)
    #
    # assert 200 == response.status_code

