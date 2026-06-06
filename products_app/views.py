from django.shortcuts import render

# Create your views here.
def product_list(request):
    # additional logic (get data from db, validate forms, etc.) can be added here
    return render(request, 'products/product_list.html')

def about(request):
    return render(request, 'products/about.html')