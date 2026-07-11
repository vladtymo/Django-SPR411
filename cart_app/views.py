from django.shortcuts import get_object_or_404, render, redirect

from cart_app.cart import get_cart_items
from products_app.models import Product

CART_SESSION_ID = 'cart'

# Create your views here.
def cart_list(request):

    products = Product.objects.all()
    cart_ids = get_cart_items(request)

    cart_items = [product for product in products if product.id in cart_ids]

    return render(request, 'cart/index.html', {'cart_items': cart_items, 'total_price': sum(item.price for item in cart_items)})

def add_to_cart(request, product_id, return_url=None):
    get_object_or_404(Product, id=product_id)

    add_to_cart(request, product_id)
     
    if return_url:
        return redirect(return_url)
    
    return render(request, 'cart/index.html')


def delete_from_Cart(request, product_id, return_url=None):
    # TODO: implement 
    return render(request, 'cart/index.html')