from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from shop.models import Product, Order


def catalog(request):
    products = Product.objects.filter(is_available=True)
    return render(request, 'shop/catalog.html', {'products': products})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'shop/product_detail.html', {'product': product})


# user=request.user
# user_id=request.user.id
# Сделать что бы были видны только азказы текузего авторизированного пользователя
# Добавить поле User в модель ордер.
# проверить что создание заказа работает корректно
def orders(request):
    if not request.user.is_authenticated:
        return redirect('login')
    orders_ = Order.objects.filter(user=request.user)
    return render(request, 'shop/orders.html', {'orders': orders_})


def create_order(request, id):
    product = Product.objects.get(id=id)
    user = request.user.id
    if request.method == 'POST':
        Order.objects.create(
            product=product,
            delivery_address=request.POST['delivery_address'],
            user=user,
        )
        return redirect('orders')
    return render(request, 'shop/create_order.html', {'product': product})
