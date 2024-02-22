from django.urls import path
from shop.views import *

urlpatterns = [
    path('catalog/', catalog, name='catalog'),
    path('product_detail/<int:id>/', product_detail, name='product_detail'),
    path('orders/', orders, name='orders'),
    path('create_order/<int:id>/', create_order, name='create_order'),

]
