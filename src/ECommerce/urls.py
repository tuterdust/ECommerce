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

from main import views as mainViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', mainViews.home, name='home'),

    url(r'^products/', mainViews.products, name='products'),
    url(r'^cart/', mainViews.cart, name='cart'),
    url(r'^about/', mainViews.about, name='about'),
    url(r'^contact/', mainViews.contact, name='contact'),
    url(r'^guide/', mainViews.guide, name='guide'),
    url(r'^product/', mainViews.product, name='product'),

    url(r'^test/', mainViews.test, name='test'),
]
