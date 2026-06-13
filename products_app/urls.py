from django import views
from django.urls import path
from products_app import views

urlpatterns = [
    path('', views.product_list, name='index'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
]
