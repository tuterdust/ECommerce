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

# Temporary: must required product id later
def product(request):
    context = {}
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


def test(request):
    context = {}
    return render(request, 'test.html', context)
