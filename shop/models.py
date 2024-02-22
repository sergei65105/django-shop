from core.models import User
from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    desc = models.TextField()
    price = models.FloatField()
    discount = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0)
    stock_count = models.PositiveIntegerField()
    is_available = models.BooleanField()

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.SET_NULL, null=True)
    delivery_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
