"""ECommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^guide/', views.guide, name='guide'),
    url(r'^sign_in/', views.sign_in, name='sign_in'),
    url(r'^sign_out/', views.sign_out, name='sign_out'),
    url(r'^sign_up/', views.sign_up, name='sign_up'),
    url(r'^user/$', views.profile, name='profile'),
    url(r'^user/orders/$', views.order_history, name='order_history'),
    url(r'^products/', views.products_listing, name='products_listing'),
    url(r'^product/(?P<p_id>[0-9]+)/', views.product_detail, name='product_detail'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^checkout/', views.checkout, name='checkout'),
    url(r'^payment/', views.payment, name='payment'),
    url(r'^order_detail/(?P<id>\w{0,9999})/$', views.order_detail, name='order_detail'),

]
