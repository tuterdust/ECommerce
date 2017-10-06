# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect

def home(request):
    context = {}
    template = 'home.html'
    return render(request, 'home.html', context)

def products(request):
    context = {}
    return render(request, 'products_listing.html', context)

# Temporary: must required product id later, put it in url too boi
def product(request):
    static_path = "/static/img/"
    context = {
        "productID": 1,
        "productName": "Arabiga 1 pouch",
        "productPrice": 2000,
        "productDescription": "BestCoffeeEver",
        "productPicture": static_path + "coffee_1.png",
        "productStock": 20
    }
    return render(request, 'product_detail.html', context)

def cart(request):
    context = {}
    return render(request, 'cart.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def guide(request):
    context = {}
    return render(request, 'guide.html', context)
