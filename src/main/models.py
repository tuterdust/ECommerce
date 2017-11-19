# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# TODO (doing): model Product
# No proving correctly
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    description = models.TextField()
    img_url = models.CharField(max_length=200)
    def __str__(self):
        return self.name

# TODO: model User

# TODO: model Order
class Order(models.Model):
    order_list = ArrayField(models.ForeignKey(Product))
    amount = ArrayField(models.IntegerField())
    date = IntegerField()
    # TODO: DateTimeField for date ordering
