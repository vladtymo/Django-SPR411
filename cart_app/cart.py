from django.shortcuts import get_object_or_404, render, redirect
from products_app.models import Product

CART_SESSION_ID = 'cart'

def get_cart_items(request):
    return request.session.get(CART_SESSION_ID, [])

def add_to_cart(request, product_id):
    request.session[CART_SESSION_ID] = [product_id] + get_cart_items(request)

def delete_from_cart(request, product_id):
    cart_items = get_cart_items(request)

    if product_id in cart_items:
        cart_items.remove(product_id)
        
    request.session[CART_SESSION_ID] = cart_items