from django.contrib import admin

from products_app.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name', 'description')
    list_filter = ('price',)

# Register your models here.
admin.site.register(Product, ProductAdmin)