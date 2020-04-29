from django.urls import path
from . import views
from prod.views import BootstrapFilterView
from products.views import product_list
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', views.home, name='app-home'),
    path('about/', views.about, name='about-page'),
    path('appliances/', views.appliances, name='app-page'),
    path('productsNew/', views.productsNew, name='app-product'),
    path('profile/', PostListView.as_view(), name='app-profile'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('bootstrap_form/', BootstrapFilterView, name='bootstrap-form'),
    path('products/', product_list, name='product-list')
]