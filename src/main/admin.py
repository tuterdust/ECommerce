# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product, SelectedProduct, Order, User

admin.site.register(Product)

#Debugging
admin.site.register(SelectedProduct)
admin.site.register(Order)
admin.site.register(User)
