from django.conf.urls import url

from .views import BootstrapFilterView

app_name = 'prod'

urlpatterns = [
    url('bootstrap_form/', BootstrapFilterView, name='bootstrap-form')
]