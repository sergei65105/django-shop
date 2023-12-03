from django.shortcuts import render


def catalog(request):
    return render(request, 'shop/catalog.html')


def product_detail(request):
    return render(request, 'shop/product_detail.html')


def orders(request):
    return render(request, 'shop/orders.html')


def create_order(request):
    return render(request, 'shop/create_order.html')
