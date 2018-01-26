from django.db import models
from django.db import connection
from django.shortcuts import render,redirect

class restaurantInfo(models.Model):
    restaurantname=models.CharField(max_length=50,null=False)
    foodtype=models.CharField(max_length=15,null=False)
    address=models.CharField(max_length=50,null=False)
    phone=models.CharField(max_length=50)
    # website=models.URLField(max_length=500)
    class Meta:
        db_table='restaurantInfo'