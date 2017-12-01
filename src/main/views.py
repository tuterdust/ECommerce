# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django import template
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from forms import *

current_user = User.objects.get(email="default")

def home(request):
    global current_user
    context = { "current_user": current_user }
    template = 'home.html'
    return render(request, 'home.html', context)

@csrf_exempt
def product_detail(request, p_id):
    global current_user
    product = get_object_or_404(Product, pk=p_id)
    if request.method == "POST":
        form = AddToCartForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            amount = data["amount"]
            if amount < 1:
                context = { "current_user": current_user, "add_error": "Invalid amount", "form": form, "product": product }
                return render(request, 'product_detail.html', context)
            elif amount > product.stock:
                context = { "current_user": current_user, "add_error": "Stock is not enough.", "form": form, "product": product }
                return render(request, 'product_detail.html', context)
            else:
                # TODO: Add product to cart
                context = { "current_user": current_user, "add_success": True, "form": form, "product": product }
                return render(request, 'product_detail.html', context)
        else:
            context = { "current_user": current_user, "add_error": "Some input is error, please try again.", "form": form, "product": product }
            return render(request, 'product_detail.html', context)
    else:
        form = AddToCartForm()
        context = { "current_user": current_user, "form": form, "product": product }
        return render(request, 'product_detail.html', context)

@csrf_exempt
def products_listing(request):
    global current_user
    products = Product.objects.all()
    if request.method == "POST":
        form = AddToCartForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            amount = data["amount"]
            product_id = data["product_id"]
            target_product = Product.objects.get(id=product_id)
            if amount > target_product.stock:
                context = { "current_user": current_user, "add_error": "Stock is not enough.", "form": form, "products": products }
                return render(request, 'products_listing.html', context)
            else:
                # TODO: Add 1 product to cart
                context = { "current_user": current_user, "add_success": True, "form": form, "products": products }
                return render(request, 'products_listing.html', context)
    else:
        context = { "current_user": current_user, "products": products }
        return render(request, 'products_listing.html', context)

def cart(request):
    global current_user

    if request.method == "POST":
        selected_product = request.POST.get('selected_product', '')
        print(str(selected_product))
        # current_user.cart_items.filter(pk=selected_product.pk).remove()

    cart_arr = []
    totalAmount = 0
    user_incart = current_user.cart_items.all()
    for p in user_incart:
        temp_amount = 0
        product =  Product.objects.get(pk=p.product_key.pk)
        temp_amount = p.amount * product.price
        cart_arr.append((product, p.amount, temp_amount, p))
        totalAmount += p.amount * product.price
    context = { "current_user": current_user, "incart": cart_arr, "total_amount": totalAmount}
    return render(request, 'cart.html', context)

def about(request):
    global current_user
    context = {}
    return render(request, 'about.html', context)

def contact(request):
    global current_user
    context = {}
    return render(request, 'contact.html', context)

def guide(request):
    global current_user
    context = {}
    return render(request, 'guide.html', context)

@csrf_exempt
def profile(request):
    global current_user

    if request.method == 'POST':
        old_email = current_user.email
        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        if old_email != 'default':
            current_user.firstname = firstname
            current_user.lastname = lastname
            current_user.email = email
            current_user.address = address
            current_user.save()

    context = { "current_user": current_user, "user": current_user }
    return render(request, 'profile.html', context)

def order_history(request):
    global current_user
    order_arr = []
    for order in current_user.order_history.all():
        selected_products = order.order_list.all()
        totalAmount = 0
        for p in selected_products:
            product =  Product.objects.get(pk=p.product_key.pk)
            totalAmount += p.amount * product.price
        order_arr.append((order, totalAmount))

    context = {
        "current_user": current_user,
        "user": current_user,
        "order_arr": order_arr
    }
    return render(request, 'order_history.html', context)

def sign_in(request):
    global current_user
    if current_user.email != 'default':
        if request.method == "POST":
            current_user = User.objects.get(email="default")
            current_user.save()
            context = { "current_user": current_user }
            return render(request, 'sign_in.html', context)
        else:
            context = { "current_user": current_user }
            return render(request, 'sign_out.html', context)
    else:
        if request.method == "POST":
            form = SignInForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                email = data["email"]
                password = data["password"]
                try:
                    user = User.objects.get(email=email, password=password)
                except User.DoesNotExist:
                    user = None
                if user != None or email == "default":
                    current_user = user
                    context = { "current_user": current_user, "sign_in_complete": True }
                    return render(request, 'home.html', context)
                else:
                    context = { "current_user": current_user, "sign_in_error": "Wrong email or password" }
                    return render(request, 'sign_in.html', context)
            else:
                context = { "current_user": current_user, "form": form, "sign_in_error": "Wrong email or password" }
                return render(request, 'sign_in.html', context)
        else:
            form = SignInForm()
            context = { "current_user": current_user, "form": form }
            return render(request, 'sign_in.html', context)

def sign_out(request):
    global current_user
    current_user = User.objects.get(email="default")
    context = { "current_user": current_user }
    return render(request, 'sign_out.html', context)

def sign_up(request):
    global current_user
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
                context = { "current_user": current_user, "form": form, "sign_up_error": "Wrong confirming password" }
                return render(request, 'sign_up.html', context)
            same_email_user = User.objects.filter(email=email)
            if same_email_user:
                context = { "current_user": current_user, "form": form, "sign_up_error": "This email has been used" }
                return render(request, 'sign_up.html', context)
            u = User(email=email, password=password, firstname=firstname, lastname=lastname, address=address)
            u.save()
            context = { "current_user": current_user, "sign_up_complete": True }
            return render(request, 'sign_up.html', context)
        else:
            context = { "current_user": current_user, "form": form, "sign_up_error": "Some input is not correct to requirement." }
            return render(request, 'sign_up.html', context)
    else:
        form = SignUpForm()
        context = { "current_user": current_user, "form": form }
        return render(request, 'sign_up.html', context)

def checkout(request):
    global current_user
    context = { "current_user": current_user }
    return render(request, 'checkout.html', context)

def payment(request):
    global current_user
    context = { "current_user": current_user }
    return render(request, 'payment.html', context)

def order_detail(request, id):
    global current_user
    totalAmount = 0
    product_arr = []
    order = Order.objects.get(pk=id)
    selected_products = order.order_list.all()
    for p in selected_products:
        product =  Product.objects.get(pk=p.product_key.pk)
        product_arr.append((product, p.amount))
        totalAmount += p.amount * product.price
    context = {
        "current_user": current_user,
        "order": order,
        "total_amount": totalAmount,
        "p_arr": product_arr
    }
    return render(request, 'order_detail.html', context)
