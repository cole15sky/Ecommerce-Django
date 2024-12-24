from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def about(request):
    return render(request, 'about.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')  # Use .get() here
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a specific page after login
            else:
                return render(request, 'login.html', {'error': 'Invalid username or password'})
        else:
            return render(request, 'login.html', {'error': 'Both fields are required'})
    return render(request, 'login.html')



def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')
