from mixer.backend.django import mixer
import pytest

@pytest.mark.django_db
class TestModels:

    def test_product__str__(self):
        products = mixer.blend('products.Product', price=1)
        assert 'Sam Ade' == True

    def test_product__str__(self):
        products = mixer.blend('products.Product', price=0)
        #assert 'Elizabeth Jackson' == False