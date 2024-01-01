from django.db import models
from datetime import date
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


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    order_id = models.CharField(max_length = 100, unique = True)
    order_no = models.CharField(max_length = 40)
    total_amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    payment_status = models.BooleanField(default = False)
    created_at = models.DateField(default = date.today)
    payment_id = models.CharField(max_length = 100, unique = True, null = True)
    signature_id = models.CharField(max_length = 100, unique = True, null = True)
   
    
    class Meta:
        db_table = 'order_tb'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE)   
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    status = models.CharField(default = 'order placed',max_length = 100 )
    packed_date = models.DateField(default = date.today, null = True)
    cancelled_date = models.DateField(default = date.today, null = True)
    cancellation_reason = models.CharField(max_length = 100)
    delivery_out = models.DateField(default = date.today, null = True)
    delivered_date = models.DateField(default = date.today, null = True)

    
    class Meta:
        db_table = 'orderItem_tb'