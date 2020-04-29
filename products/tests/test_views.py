from django.test import RequestFactory
from django.urls import reverse, resolve
from mixer.backend.django import mixer
from django.contrib.auth.models import User, AnonymousUser
from products.views import product_list
from mixer.backend.django import mixer
from django.test import TestCase
import pytest

@pytest.mark.django_db
class TestViews(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestViews, cls).setUpClass()
        mixer.blend('products.Product')
        cls.factory = RequestFactory()

    def test_product_list_authenticated(self):
        url = reverse('product-list')
        request = self.factory.get(url)
        request.user = mixer.blend(User)

        response = product_list(request)
        assert response.status_code == 200
        
    def test_product_list_unauthenticated(self):
        url = reverse('product-list')
        request = self.factory.get(url)
        request.user = AnonymousUser()

        response = product_list(request)
        #assert response.status_code == 300
        