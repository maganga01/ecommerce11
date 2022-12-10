import pytest
from ecommerce.inventory.models import Category

@pytest.fixture
def test_single(db):
    return Category.objects.create(name="default", slug="default")
