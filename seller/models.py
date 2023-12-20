from django.db import models
from eKart_admin.models import Category

# Create your models here.

class Seller(models.Model):
    first_name = models.CharField(max_length =  20)
    last_name =  models.CharField(max_length =  20)
    company_name = models.CharField(max_length = 20)
    email =  models.CharField(max_length =  50)
    gender = models.CharField(max_length = 10)
    city = models.CharField(max_length = 20)
    country = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    pic = models.ImageField(upload_to = 'seller/')
    login_id = models.IntegerField(null = True)
    password = models.CharField(max_length = 20)
    account_no = models.BigIntegerField()
    bank_name = models.CharField(max_length = 20)
    branch_name = models.CharField(max_length = 20)
    ifsc = models.CharField(max_length = 20)

    status = models.CharField(max_length = 20, default = 'pending')

    class Meta:
        db_table = 'seller_tb'


class Product(models.Model):
    product_no = models.CharField(max_length =  30)
    product_name =  models.CharField(max_length =  20)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete = models.CASCADE)
    description =  models.CharField(max_length =  200)
    stock = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to = 'product/')
    rating = models.FloatField(default = 0)
    status = models.CharField(max_length = 20, default = 'available')
    
    class Meta:
        db_table = 'product_tb'