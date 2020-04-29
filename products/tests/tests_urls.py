from django.urls import reverse, resolve
import pytest



class TestUrls:

    def test_detail_url(self):
        path = reverse('product-list', kwargs={'': 1})
        assert resolve(path).view_name == 'product-list'