from itertools import product
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic



# Create your models here.

class couture(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.CharField(max_length=1000)
    code=models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    size = models.TextField()
    

    class Product(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()
        price = models.DecimalField(max_digits=8, decimal_places=2)
        size = models.TextField()


    class User(models.Model):
        username = models.CharField(max_length=100)
        first_name=models.TextField()
        last_name= models.TextField()
        email= models.TextField()
        password=models.TextField()

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(couture, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.title} in {self.cart}"
