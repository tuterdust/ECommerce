# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Product, User
from forms import SignInForm, SignUpForm

def home(request):
    context = {}
    template = 'home.html'
    return render(request, 'home.html', context)

def product_detail(request, p_id):
    product = get_object_or_404(Product, pk=p_id)
    context = { "product": product }
    return render(request, 'product_detail.html', context)

def products_listing(request):
    products = Product.objects.all()
    context = { "products": products }
    return render(request, 'products_listing.html', context)

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

def profile(request):
    context = {}
    return render(request, 'profile.html', context)

def order_history(request):
    products = {
        "product": [{
            "name": "coffee_1",
            "price": 500,
            "amount": 2
        },
        {
            "name": "coffee_2",
            "price": 1000,
            "amount": 2
        },
        {
            "name": "coffee_3",
            "price": 500,
            "amount": 2
        }],
        "totalAmount": 4000
    }

    orders = [{"orderID": "001", "products": products, "totalAmount": 4000, "date": "xx/xx/xxxx","status": 0},
        {"orderID": "002", "products": products, "totalAmount": 1000, "date": "xx/xx/xxxx","status": 1},
        {"orderID": "003", "products": products, "totalAmount": 3500, "date": "xx/xx/xxxx","status": 1},
        {"orderID": "003", "products": products, "totalAmount": 1000, "date": "xx/xx/xxxx","status": 2}]# 0 = unpaid, 1 = paid, 2 = on_cart

    context = {
        "user": {
            "orders": orders
        }
    }
    return render(request, 'order_history.html', context)

def sign_in(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            email = data["email"]
            password = data["password"]
            user = User.objects.all().filter(email=email, password=password)
            # TODO Bug: when get this user, it's just query set that cannot use any attributes, it will be error if call attributes
            if user:
                context = { "sign_in_complete": True }
                return render(request, 'home.html', context)
            else:
                context = { "sign_in_error": "Wrong email or password" }
                return render(request, 'sign_in.html', context)
            context = { "sign_in_complete": True }
            return render(request, 'home.html', context)
        else:
            context = { "form": form, "sign_in_error": "Wrong email or password" }
            return render(request, 'sign_in.html', context)
    else:
        form = SignInForm()
        context = { "form": form }
        return render(request, 'sign_in.html', context)

def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            email = data["email"]
            password = data["password"]
            confirm_password = data["confirm_password"]
            firstname = data["firstname"]
            lastname = data["lastname"]
            address = data["address"]
            if password != confirm_password:
                context = { "form": form, "sign_up_error": "Wrong confirming password" }
                return render(request, 'sign_up.html', context)
            same_email_user = User.objects.filter(email=email)
            if same_email_user:
                context = { "form": form, "sign_up_error": "This email has been used" }
                return render(request, 'sign_up.html', context)
            u = User(email=email, password=password, firstname=firstname, lastname=lastname, address=address)
            u.save()
            context = { "sign_up_complete": True }
            return render(request, 'sign_up.html', context)
        else:
            context = { "form": form, "sign_up_error": "Some input is not correct to requirement." }
            return render(request, 'sign_up.html', context)
    else:
        form = SignUpForm()
        context = { "form": form }
        return render(request, 'sign_up.html', context)

def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)

def payment(request):
    context = {}
    return render(request, 'payment.html', context)

def order_detail(request, id):
    products = {
        "product": [{
            "name": "coffee_1",
            "price": 500,
            "amount": 2
        },
        {
            "name": "coffee_2",
            "price": 1000,
            "amount": 2
        },
        {
            "name": "coffee_3",
            "price": 500,
            "amount": 2
        }],
        "total_amount": 4000
    }
    context = {
        "orderID": "001",
        "products": products,
        "date": "xx/xx/xxxx",
        "status": 0
    }
    return render(request, 'order_detail.html', context)
