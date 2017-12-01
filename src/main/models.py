# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.db import models
from django.core.validators import MinLengthValidator

class Product(models.Model):
    name = models.CharField(max_length=100)         # Product name
    category = models.CharField(max_length=30)      # Product category: Coffee or Tea
    price = models.IntegerField(default=0)          # Price per piece of product
    stock = models.IntegerField(default=0)          # Stock available of product
    description = models.TextField()                # Product description
    img_url = models.CharField(max_length=200)      # Image file url for showing of product
    def __str__(self):
        return self.name

# In developing

class SelectedProduct(models.Model):
    product_key = models.ForeignKey(Product)
    amount = models.IntegerField(default=0)
    def __str__(self):
        product = Product.objects.get(pk=self.product_key.pk)
        return "%s X %s" % (product.name, self.amount)

class Order(models.Model):
    order_list = models.ManyToManyField(SelectedProduct)
    date = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return "Order %s " % (self.pk)

class User(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=25, validators=[MinLengthValidator(8)])
    address = models.CharField(max_length=2000)
    order_history = models.ManyToManyField(Order)
    cart_items = models.ManyToManyField(SelectedProduct)
    def __str__(self):
        return self.firstname + " " + self.lastname
