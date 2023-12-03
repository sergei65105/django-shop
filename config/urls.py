from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from shop.views import *
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/catalog/', catalog),
    path('shop/product_detail/', product_detail),
    path('shop/orders/', orders),
    path('shop/create_order/', create_order),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

