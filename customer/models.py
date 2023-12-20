from django.db import models

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