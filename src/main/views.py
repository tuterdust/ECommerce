# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect

def home(request):
    context = {}
    return render(request, 'home.html', context)
