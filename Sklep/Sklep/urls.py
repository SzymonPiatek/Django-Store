from django.contrib import admin
from django.urls import path
from Produkty.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('kategoria/<id>', kategoria, name='kategoria'),
    path('produkt/<id>', produkt, name='produkt'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)