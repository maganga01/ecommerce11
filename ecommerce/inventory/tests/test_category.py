from ecommerce.inventory.models import Category


def test_create_category(single_category):
    new_category = single_category 
    get_category = category.objects.all().first()
    assert new_category.id == category.id