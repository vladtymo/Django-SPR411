from django import views
from django.contrib import admin
from django.urls import include, path
from django_shop_app import settings
from django.conf.urls.static import static

from products_app import views

urlpatterns = [
    path('', include('products_app.urls')),
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)