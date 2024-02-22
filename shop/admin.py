from django.contrib import admin
from shop.models import Product, Order


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_editable = ('name',)
    list_display = (
        'id',
        'name',
        'desc',
        'image',
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_editable = ('delivery_address',)
    list_display = (
        'id',
        'product',
        'delivery_address',
        'created_at',
    )