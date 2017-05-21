# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html', {'STATIC_URL': settings.STATIC_URL})