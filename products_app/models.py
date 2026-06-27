from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('clothing', 'Clothing'),
        ('books', 'Books'),
        ('furniture', 'Furniture'),
        ('others', 'Others'),
    ]

    name = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='product_images/', null=True)
    image_url = models.URLField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='others')
    discount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.category}'