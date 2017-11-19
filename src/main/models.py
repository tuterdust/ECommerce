# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    description = models.TextField()
    img_url = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Order(models.Model):
    order_list = ArrayField(models.ForeignKey(Product))
    amount = ArrayField(models.IntegerField())
    date = models.DateTimeField(default=datetime.now())

class User(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharFiled(min_length=8, max_length=25)
    address = models.CharField(max_length=2000)
    order = ArrayField(models.ForeignKey(Order))
    cart_product = ArrayField(models.ForeignKey(Product))
    cart_amount = ArrayField(models.IntegerField())
