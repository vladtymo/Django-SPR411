from django import views
from django.urls import path
from cart_app import views

urlpatterns = [
    path('', views.cart_list, name='cart'),
    path('add/<int:product_id>/<path:return_url>/', views.add_to_cart, name='add_to_cart'),
]
