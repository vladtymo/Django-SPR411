from django import views
from django.urls import path
from products_app import views

urlpatterns = [
    path('', views.product_list, name='index'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('products/admin/', views.get_admin_list, name='admin'),
]
