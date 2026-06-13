from django import views
from django.contrib import admin
from django.urls import include, path
from products_app import views

urlpatterns = [
    path('', include('products_app.urls')),
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls),
]
