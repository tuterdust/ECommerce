# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django import template
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from forms import SignInForm, SignUpForm

current_user = User.objects.create(email="default")
current_user.save()

def home(request):
    global current_user
    context = {}
    template = 'home.html'
    return render(request, 'home.html', context)

def product_detail(request, p_id):
    global current_user
    product = get_object_or_404(Product, pk=p_id)
    context = { "product": product }
    return render(request, 'product_detail.html', context)

def products_listing(request):
    global current_user
    products = Product.objects.all()
    context = { "products": products }
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
    context = { "incart": cart_arr, "total_amount": totalAmount}
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

    context = { "user": current_user }
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
                if user != None:
                    context = { "sign_in_complete": True }
                    current_user = user
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
    global current_user
    context = {}
    return render(request, 'checkout.html', context)

def payment(request):
    global current_user
    context = {}
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
        "order": order,
        "total_amount": totalAmount,
        "p_arr": product_arr
    }
    return render(request, 'order_detail.html', context)
