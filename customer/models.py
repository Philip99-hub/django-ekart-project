from django.db import models
from seller.models import Product

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length =  20)
    last_name =  models.CharField(max_length =  20)
    email =  models.CharField(max_length =  50)
    gender = models.CharField(max_length = 10)
    city = models.CharField(max_length = 20)
    country = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)

    class Meta:
        db_table = 'customer_tb'

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 1)
    price = models.FloatField()


    class Meta:
        db_table = 'cart_tb'