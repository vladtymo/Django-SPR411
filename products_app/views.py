from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
    
from products_app.forms import product
from products_app.models import Product

products_old = [
    {
        'id': 1,
        'name': 'iPhone X',
        'description': 'Description for product 1',
        'price': 19.99,
        'stock': 10,
        'category': 'electronics',
        'discount': 10,
        'image': 'https://content1.rozetka.com.ua/goods/images/big/221203654.jpg',
    },
    {
        'id': 2,
        'name': 'Samsung Galaxy S21',
        'description': 'Description for product 2',
        'price': 29.99,
        'stock': 5,
        'category': 'clothing',
        'discount': 20,
        'image': 'https://content.rozetka.com.ua/goods/images/big/487792065.jpg',
    },
    {
        'id': 3,
        'name': 'MacBook Pro',
        'description': 'Description for product 3',
        'price': 9.99,
        'stock': 20,
        'category': 'books',
        'discount': 0,
        'image': 'https://content1.rozetka.com.ua/goods/images/big_tile/655338574.jpg',
    },
]

# Create your views here.
def product_list(request):
    # additional logic (get data from db, validate forms, etc.) can be added here
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, product_id):
    # product = Product.objects.get(id=product_id) # pk=product_id
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

def about(request):
    return render(request, 'products/about.html')

def get_admin_list(request):
    products = Product.objects.all()
    return render(request, 'products/admin.html', {'products': products})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()

    messages.error(request, 'Product deleted successfully!')
    
    return redirect('/products/admin/')

def create_product(request):
    if request.method == 'POST':
        print('POST', request.POST)
        form = product.ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully!')
            return redirect('/products/admin/')
        else:
            return render(request, 'products/create.html', {'form': form})
        
    form = product.ProductForm()
    return render(request, 'products/create.html', {'form': form})

def edit_product(request, product_id, return_url=None):
    item = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = product.ProductForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            if return_url:
                return redirect(return_url)
            return redirect('/products/admin/')
        else:
            return render(request, 'products/edit.html', {'form': form})

    
    form = product.ProductForm(instance=item)
    return render(request, 'products/edit.html', {'form': form})
