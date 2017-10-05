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

def cart(request):
    context = {}
    return render(request, 'carts.html', context)

def about(request):
    context = {}
    return render(request, 'about_us.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def guide(request):
    context = {}
    return render(request, 'guide.html', conotext)


def test(request):
    context = {}
    return render(request, 'test.html', context)
