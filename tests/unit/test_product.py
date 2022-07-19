import pytest
from base.models import Product

@pytest.mark.django_db
def test_create_product_by_id():
    p = Product.objects.create(
        name=" Product Name ",
        price=0,
        brand="Sample brand ",
        countInStock=0,
        category="Sample category",
        description=" "
    )

    assert p._id == 1

@pytest.mark.django_db
def test_delete_product_by_id():
    product = Product.objects.create(
        name="Tesle3x",
        price=100000,
        brand="Tesla",
        countInStock=2,
        category="electric car",
        description="red car"
    )
    # deleting a product
    product.delete()

    assert product._id== None

@pytest.mark.django_db()
def test_create_product_by_type():
        p = Product.objects.create(
            name=" Product Name ",
            price=0,
            brand="Sample brand ",
            countInStock=0,
            category="Sample category",
            description=" "
        )

        assert isinstance(p,Product) is True

@pytest.mark.django_db()
def test_create_product_by_data():
    p = Product.objects.create(
        name=" Product Name ",
        price=0,
        brand="Sample brand ",
        countInStock=0,
        category="Sample category",
        description=" "
        )

    assert p.name == " Product Name "