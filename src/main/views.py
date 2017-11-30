# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
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
    user_incart = user.cart_items.all()
    context = { "incart": user_incart}
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

@csrf_exempt
def profile(request):
    user = User.objects.get(email="tuter555awesome@gmail.com")

    if request.method == 'POST':
        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        user.firstname = firstname
        user.lastname = lastname
        user.email = email
        user.address = address
        user.save()

    context = { "user": user }
    return render(request, 'profile.html', context)

def order_history(request):
    user = User.objects.get(email="tuter555awesome@gmail.com")
    order_arr = []
    for order in user.order_history.all():
        selected_products = order.order_list.all()
        totalAmount = 0
        for p in selected_products:
            product =  Product.objects.get(pk=p.product_key.pk)
            totalAmount += p.amount * product.price
        order_arr.append((order, totalAmount))

    context = {
        "user": user,
        "order_arr": order_arr
    }
    return render(request, 'order_history.html', context)

def sign_in(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            email = data["email"]
            password = data["password"]
            user = User.objects.all().get(email=email, password=password)
            if user:
                context = { "sign_in_complete": True }
                return render(request, 'home.html', context)
            else:
                context = { "sign_in_error": "Wrong email or password" }
                return render(request, 'sign_in.html', context)
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
    totalAmount = 0
    product_arr = []
    order = Order.objects.get(pk=id)
    selected_products = order.order_list.all()
    for p in selected_products:
        product =  Product.objects.get(pk=p.product_key.pk)
        product_arr.append((product, p.amount))
        totalAmount += p.amount * product.price
    context = {
        "order": order,
        "total_amount": totalAmount,
        "p_arr": product_arr
    }
    return render(request, 'order_detail.html', context)
