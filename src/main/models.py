# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# TODO (doing): model Product
# No proving correctly
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    def __str__(self):
        return self.name

# TODO: model User
# TODO: model Order
