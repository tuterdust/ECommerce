# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import RegexValidator

class Product(models.Model):
    name = models.CharField(max_length=100)         # Product name
    category = models.CharField(max_length=30)      # Product category: Coffee or Tea
    price = models.IntegerField(default=0)          # Price per piece of product
    stock = models.IntegerField(default=0)          # Stock available of product
    description = models.TextField()                # Product description
    img_url = models.CharField(max_length=200)      # Image file url for showing of product
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
    password = models.CharField(validators=[RegexValidator(regex='^.{8}$', message='Length has to be 8', code='nomatch')], max_length=25)
    address = models.CharField(max_length=2000)
    order = ArrayField(models.ForeignKey(Order))
    cart_product = ArrayField(models.ForeignKey(Product))
    cart_amount = ArrayField(models.IntegerField())
    def __str__(self):
        return self.firstname
