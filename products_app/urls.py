from django import views
from django.urls import path
from products_app import views

urlpatterns = [
    path('', views.product_list, name='index'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('products/admin/', views.get_admin_list, name='admin'),
    path('products/create/', views.create_product, name='create_product'),
    path('products/edit/<int:product_id>/<path:return_url>/', views.edit_product, name='edit_product_with_return'),
    path('products/edit/<int:product_id>/', views.edit_product, name='edit_product'),

]
