from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from store.models import *

def dashboard(request):
    context = {
        'categories': Category.objects.all(),
        'customers': Customer.objects.all(),
        'products': Product.objects.all(),
        'orders': Order.objects.all(),
    }
    return render(request, 'customAdmin/dashboard.html', context)  

def products(request):
    objs = products.objects.all()
    return render(request,'products.html',{"objs":objs})

